
import _SnowflakeData


class SnowflakeData(_SnowflakeData.SnowflakeData):
    # Constructor
    def __init__(self, username, warehouse, role, database=None, schema=None, table=None, column_name=None,
                 col_and_or=None, get_ex_val=None, like_flag=None):
        self.__username = username
        self.__warehouse = warehouse
        self.__role = role
        self.__database = database
        self.__schema = schema
        self.__table = table
        self.__column_name = column_name
        self.__col_and_or = col_and_or
        self.__get_ex_val = get_ex_val
        self.__like_flag = like_flag

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def warehouse(self):
        return self.__warehouse

    @warehouse.setter
    def warehouse(self, value):
        self.__warehouse = value

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        self.__role = value

    @property
    def database(self):
        return self.__database

    @database.setter
    def database(self, value):
        self.__database = value

    @property
    def schema(self):
        return self.__schema

    @schema.setter
    def schema(self, value):
        self.__schema = value

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        self.__table = value

    @property
    def column_name(self):
        return self.__column_name

    @column_name.setter
    def column_name(self, value):
        self.__column_name = value

    @property
    def col_and_or(self):
        return self.__col_and_or

    @col_and_or.setter
    def col_and_or(self, value):
        self.__col_and_or = value

    @property
    def get_ex_val(self):
        return self.get_ex_val

    @get_ex_val.setter
    def get_ex_val(self, value):
        self.__get_ex_val = value

    @property
    def like_flag(self):
        return self.__like_flag

    @like_flag.setter
    def like_flag(self, value):
        self.__like_flag = value

    def build_search_query(self, inp_db=None, schema=None, table=None, column_name=None, like_flag=None,
                           col_and_or=None):
        if schema is None:
            schema = self.__schema
        if table is None:
            table = self.__table
        if column_name is None:
            column_name = self.__column_name
        if like_flag is None:
            like_flag = self.__like_flag
        if col_and_or is None:
            col_and_or = self.__col_and_or

        return _SnowflakeData.SnowflakeData.build_search_query(self, inp_db=inp_db, schema=schema, table=table,
                                                               column_name=column_name, like_flag=like_flag,
                                                               col_and_or=col_and_or)

    def snowflake_pull(self, query: str, username=None, warehouse=None, database=None, role=None,
                       sample_table: bool = False, sample_val: bool = False, table_sample: dict = None,
                       dtypes_conv=None):

        if username is None:
            username = self.__username
        if warehouse is None:
            warehouse = self.__warehouse
        if database is None:
            database = self.__database
        if role is None:
            role = self.__role

        return _SnowflakeData.SnowflakeData.snowflake_pull(self, query, un=username, wh=warehouse, db=database,
                                                           role=role, sample_table=sample_table, sample_val=sample_val,
                                                           table_sample=table_sample, dtypes_conv=dtypes_conv)


# if __name__ == '__main__':
#     import configparser
#
#     config = configparser.ConfigParser()
#     config.read('config.ini')
#
#     username = config['snowflake'].get('username')
#     warehouse = config['snowflake'].get('warehouse')
#     role = config['snowflake'].get('role')
#     database = config['snowflake'].get('database')
#
#     sf = SnowflakeData(username, warehouse, role, database=database)
#
#     # query = 'SELECT TOP 2 ACTIVITY_END_DT, PRODUCT_COMPOSITE_ID FROM  NGP_DA_PROD.POS.TO_DATE_AGG_CHANNEL_CY'
#     print(sf.snowflake_pull(sf.build_search_query(column_name='%DISTINCT%', like_flag=True))[['TABLE_CATALOG',
#                                                                                               'TABLE_SCHEMA',
#                                                                                               'COLUMN_NAME']])


