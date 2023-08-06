from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import ASYNCHRONOUS, SYNCHRONOUS
from influxdb_client import WritePrecision
from influxdb_client.client.exceptions import InfluxDBError
from influxdb_lite.attributes import Field, Tag
import datetime as dt
import time
import logging


class Client(InfluxDBClient):
    def __init__(self, url: str, token: str, org: str, name=__name__, **kwargs):
        super().__init__(url=url, token=token, org=org, **kwargs)
        self.logger = logging.getLogger(name)
        self.url = url
        self.token = token
        self.org = org
        self.query_list = []
        self.measurement = None
        self.select_list = ['_time']

    def _query_str(self):
        return '\n'.join(self.query_list)

    def query(self, measurement):
        """Defines the base query from the bucket and the name of the measurement selected. All the following
        methods need a base query to work. """
        self.measurement = measurement
        self.select_list += measurement.tags + measurement.fields
        self.query_list = [f'from(bucket: "{measurement.bucket}")',
                           f'|> filter(fn: (r) => r._measurement == "{measurement.name}")']
        return self

    def select(self, *args, method: str = 'or'):
        """ Receives a list of fields to show in resulting table of the query. If it's not called, all the columns
        will be selected by default. """
        self._check_attr(args, _type='fields')
        arg_names = [arg.name for arg in args]
        self.select_list = arg_names if '_time' in arg_names else arg_names + ['_time']
        range_idxs = [i for i in range(len(self.query_list)) if 'range' in self.query_list[i]]
        range_idx = 1 if not range_idxs else range_idxs[0]+1
        self.query_list.insert(
            range_idx,
            self._contain_or_or(column="_field", _list=self.select_list, method=method)
        )
        return self

    def _check_attr(self, args, _type: str = 'columns'):
        """Checks is args correspond to either fields, tags or columns"""
        if _type not in ('columns', 'fields', 'tags'):
            raise ValueError(f"Unrecognized type {_type} to check inside of. ")
        for arg in args:
            if not isinstance(args, (Field, Tag)):
                raise AttributeError(f'The attributes passed should be an instance of the classes Tag or Field. Received '
                                     f'{type(args)} instead.')
        for arg in args:
            if arg.name not in getattr(self.measurement, _type):
                raise ValueError(f"Field: {arg.name} is not present in measurement {self.measurement}")

    def range(self, start: (int, str, dt.datetime), stop: (int, str, dt.datetime) = None):
        """ Modifies the base query adding a specified range. This range can be either relative or absolute, this will
        depend on the start argument datatype. If start is a string (for example: '-15d'), the type will be considered
        relative and if is datetime or int, it will be considered absolute.
        If 'stop' key is not present or its value is None, now() will be considered as default. If 'start' key is not
        present method will raise an error. """
        self._validate_selection(['_time'])
        v_start, v_stop = self._validate_range(start, stop)
        self.query_list.insert(1, f"|> range(start: {v_start}, stop: {v_stop})")
        return self

    def _validate_range(self,  start: (int, float, str, dt.datetime), stop: (int, float, str, dt.datetime)):
        if stop is None:
            stop = 'now()'
        elif isinstance(stop, float):
            stop = int(stop)
        elif isinstance(stop, int) or isinstance(stop, str):
            pass
        elif isinstance(stop, dt.datetime):
            stop = self._dt_to_RFC3339(stop)
        else:
            raise ValueError(f"_type {type(stop)} not recognized. ")
        if start is None:
            raise ValueError(f"Invalid start value. ")
        elif isinstance(start, float):
            start = int(start)
        elif isinstance(start, int) or isinstance(start, str):
            pass
        elif isinstance(start, dt.datetime):
            start = self._dt_to_RFC3339(start)
        else:
            raise ValueError(f"_type {type(start)} not recognized. ")
        return start, stop

    def filter(self, *args, method: str = 'or'):
        """ Adds filter statement to query. Receives filter statements in the form Measurement.Tag == a, ...
        where the available operations are ==, >, <, >=, <= and the in_ function. 'method' arg can be either 'contains'
        or 'or'. Use or for optimized queries.
        * The 'in_' operation for fields must be used in conjunction with the select method and only one field at a time
         to work properly.
        """
        for (attr, comparator, value) in args:
            if attr in self.measurement.tags:
                if comparator != 'in':
                    self.query_list.append(f'|> filter(fn: (r) => r["{attr}"] {comparator} "{value}")')
                else:
                    self.query_list.append(self._contain_or_or(column=attr, _list=value, method=method))
            elif attr in self.measurement.fields:
                if comparator != 'in':
                    self.query_list.append(f'|> filter(fn: (r) => r["_field"] == "{attr}" and r["_value"] {comparator} {value})')
                else:
                    self.query_list.append(self._contain_or_or(column="_value", _list=value, method=method))
            else:
                ValueError(f"Unrecognized attribute {attr} given in dictionary.")
        return self

    def group_by(self, _list: list):
        """Group by the influxdb tables based on influxdb columns. """
        self._validate_selection(_list)
        self.query_list.append(f'|> group(columns: {self._parse_list_into_str(_list)})')
        return self

    def order_by(self, _list: list, desc: bool):
        """Sorts influxdb columns in descending or ascending order. """
        self._validate_selection(_list)
        self.query_list.append(f'|> sort(columns: {self._parse_list_into_str(_list)}, desc: {str(desc).lower()})')
        return self

    def pivot(self, row_keys: list = None, column_keys: list = None, value_column: str = '_value'):
        """Pivots a table based on row_keys, column_keys and a value_column. The default call pivots field sets into
        a sql-like table. """
        row_keys = ['_time'] if row_keys is None else row_keys
        column_keys = ['_field'] if column_keys is None else column_keys
        self.query_list.append(f'|> pivot(rowKey:{self._parse_list_into_str(row_keys)}, columnKey: {self._parse_list_into_str(column_keys)}, valueColumn: "{value_column}")')
        return self

    def limit(self, lmt: int):
        """Limits the amount of results to {lmt}. """
        self.query_list.append(f'|> limit(n:{lmt})')
        return self

    def last(self, field: Field = None):
        """Applies the last() command from FluxQL. """
        column = f'column:"{field.name}"' if field else ''
        self.query_list.append(f'|> last({column})')
        return self

    def exec(self):
        return self._execute()

    def _execute(self):
        return self._tables_iterator(self.query_api().query(query=self._query_str(), org=self.org))

    def all(self):
        return self.drop(['_start', '_stop']).pivot().exec()

    def raw(self):
        """Executes the resulting query. """
        return self.drop(['_start', '_stop']).exec()

    def drop(self, _list: list):
        self.query_list.append(f'|> drop(columns:{self._parse_list_into_str(_list)})')
        return self

    def to_dataframe(self):
        return self.drop(['_start', '_stop']).query_api().query_data_frame(self._query_str())

    def _contain_or_or(self, column: str, _list: list, method: str = 'contains'):
        if method == 'contains':
            _set = self._parse_list_into_str(_list) if column in self.measurement.tags else str(_list)
            return f'|> filter(fn: (r) => contains(value: r.{column}, set:{_set}))'
        elif method == 'or':
            return self._parse_or_list(column, _list)
        else:
            ValueError(f"Unrecognized method: {method}")

    @staticmethod
    def _parse_list_into_str(_list):
        _str = "["
        for _int in _list[:-1]:
            _str += f"\"{str(_int)}\","
        return _str + f"\"{str(_list[-1])}\"]"

    def _parse_or_list(self, column, _list):
        base_str = "|> filter(fn: (r) =>"
        if column in self.measurement.tags + ['_field']:
            or_list = [f" r.{column} == \"{item}\" " for item in _list]
        else:
            or_list = [f" r.{column} == {item} " for item in _list]
        return base_str + "or".join(or_list) + ")"

    def _validate_selection(self, _list):
        for column in _list:
            if column not in self.select_list:
                raise TypeError(f"Please include {column} in the select list.")

    def _dt_to_RFC3339(self, datetime_obj: dt.datetime = dt.datetime.now(), _format: str = 'long'):
        """Transform datetime object into string RFC3339 format (either in date, short or long format). Ignores
         timezone aware datetime objects. """
        if datetime_obj is not None:
            base = datetime_obj.isoformat()
            res = self._get_resolution(base)
            base = base.split('+')[0] if '+' in base else base
            if _format == 'date':
                return base.split('T')[0]
            elif _format == 'short':
                return base[:-res-1] + 'Z' if res == 6 else base + 'Z'
            elif _format == 'long':
                return base[:-res//2] + 'Z' if res == 6 else base + '.000Z'
            else:
                raise ValueError("Enter a format from 1 to 3")

    @staticmethod
    def _dt_to_unix(datetime_obj: dt.datetime = dt.datetime.now()):
        """Transform datetime object into string RFC3339 format (either in date, short or long format). Ignores
         timezone aware datetime objects. """
        if datetime_obj is not None:
            return int(time.mktime(datetime_obj.timetuple()))

    @staticmethod
    def _get_resolution(isoformat):
        if len(isoformat.split('.')) == 1:
            return -1
        else:
            return len(isoformat.split('.')[1])

    def bulk_insert(self, measurements: list, precision: str = 'ns', write_mode: str = 'SYNCHRONOUS'):
        """
        Receives a list of measurement objects or dictionaries and inserts them in bulk. At least one tag and one
        field per measure are needed. Empty-valued tags or fields will not be included.

        measurements: Can be either measurement objects or dictionaries. Dictionaries expect 'bucket', 'name',
                      'fields', 'tags' to be defined. '_time' can be optionally given. Fields and tags also expect
                      dictionaries as an input.
        precision:    Sets the precision to either seconds (s), milliseconds (ms), microseconds(us) or nanoseconds
                      (default). Precision is set for all the batch inserted. timestamp has to be an int equal to the
                      number of s, ms, us or ns since epoch. For example use time.time_ns() for default precision and
                      int(time.time()) for precision = 's'.
        """
        if isinstance(measurements[0], dict):
            self._bulk_insert_dicts(measurements, precision=precision, write_mode=write_mode)
        else:
            self._bulk_insert_measurements(measurements, precision=precision, write_mode=write_mode)

    def _bulk_insert_dicts(self, measurements: list, precision: str = 'ns', write_mode: str = 'SYNCHRONOUS'):
        sequence = []
        bucket = measurements[0]['bucket']
        for measure in measurements:
            if bucket != measure['bucket']:
                raise ValueError('Bulk insert is only supported for one bucket at a time')
            tag_set = ','.join(f"{tag}={measure['tags'][tag]}" for tag in measure['tags'])
            field_set = ','.join(f'{field}="{measure["fields"][field]}"'
                                 if isinstance(measure["fields"][field], str)
                                 else f'{field}={measure["fields"][field]}' for field in measure['fields'])
            if field_set == '':
                raise ValueError(f'Cannot insert zero fields in measurement.')
            msg = f'{measure["name"]}'
            if tag_set:
                msg += f',{tag_set}'
            msg += f' {field_set}'
            if measure.get('_time') is not None:
                msg += f' {measure["_time"]}'
            sequence.append(msg)
        self._write_batch(bucket, sequence, precision=precision, write_mode=write_mode)

    def _bulk_insert_measurements(self, measurements: list, precision: str = 'ns', write_mode: str = 'SYNCHRONOUS'):
        sequence = []
        bucket = measurements[0].bucket
        for measure in measurements:
            if bucket != measure.bucket:
                raise ValueError('Bulk insert is only supported for one bucket at a time')
            values = measure.get_values()
            tag_set = ','.join(f'{tag}={values[tag]}'
                               for tag in measure.tags if values.get(tag, None) is not None)
            field_set = ','.join(f'{field}="{values[field]}"'
                                 if isinstance(values[field], str)
                                 else f'{field}={values[field]}'
                                 for field in measure.fields if values.get(field, None) is not None)
            if tag_set == '' or field_set == '':
                raise ValueError(f'Cannot insert zero fields in measurement.')
            if values.get('_time', None) is not None:
                sequence.append(f'{measure.name},{tag_set} {field_set} {values["_time"]}')
            else:
                sequence.append(f'{measure.name},{tag_set} {field_set}')
        self._write_batch(bucket, sequence, precision=precision, write_mode=write_mode)

    def _write_batch(self, bucket: str, batch: list, precision: str = 'ns', write_mode: str = 'SYNCHRONOUS'):
        if write_mode == 'SYNCHRONOUS':
            with self.write_api(write_options=SYNCHRONOUS) as write_api:
                write_api.write(bucket=bucket, org=self.org, record='\n'.join(batch),
                                write_precision=getattr(WritePrecision, precision.upper()))
        elif write_mode == 'ASYNCHRONOUS':
            before = time.time()
            with self.write_api(success_callback=self.on_success,
                                error_callback=self.on_error, retry_callback=self.on_retry) as write_api:
                write_api.write(bucket=bucket, org=self.org, record='\n'.join(batch),
                                write_precision=getattr(WritePrecision, precision.upper()))
            after = time.time()
            self.logger.info(f'BATCH TIME {after-before}')

    def _tables_iterator(self, tables):
        """Implements an iterator over resulting tables of a query so that the user can easily iterate the resulting
        rows"""
        for table in tables:
            for record in table.records:
                yield self.cast_types(record.values)

    def cast_types(self, values: dict):
        for key in values:
            if key in self.measurement.tags:
                values[key] = getattr(self.measurement, key).cast(values[key])
        return values

    def on_success(self, conf: (str, str, str), data: str):
        pass

    def on_error(self, conf: (str, str, str), data: str, exception: InfluxDBError):
        self.logger.error(f"Cannot write batch: {conf}, data: {data} due: {exception}")

    def on_retry(self, conf: (str, str, str), data: str, exception: InfluxDBError):
        pass

    def check_health(self):
        return self.ping()
