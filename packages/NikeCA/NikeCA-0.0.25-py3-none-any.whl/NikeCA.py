
import _SnowflakeData


class SnowflakeData(_SnowflakeData.SnowflakeData):
    """
        A class for interacting with Snowflake databases and executing queries.
        Inherits from _SnowflakeData.SnowflakeData.
        """

    # Constructor
    def __init__(self, username: str, warehouse: str, role: str, database: str = None, schema: str = None,
                 table: str = None, column_name: str = None, col_and_or: str = None, get_ex_val: bool = None,
                 like_flag: bool = None):
        """
        Initializes a new instance of the SnowflakeData class with the specified parameters.

        Parameters:
            username (str): The Snowflake account username.
            warehouse (str): The Snowflake warehouse to use.
            role (str): The Snowflake role to use.
            database (str, optional): The Snowflake database to use (default is None).
            schema (str, optional): The Snowflake schema to use (default is None).
            table (str, optional): The Snowflake table to use (default is None).
            column_name (str, optional): The name of the column to search (default is None).
            col_and_or (str, optional): The AND/OR operator to use between search criteria (default is None).
            get_ex_val (bool, optional): Whether to return exact matches only (default is None).
            like_flag (bool, optional): Whether to use the LIKE operator for search criteria (default is None).
        """

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

    # Getter and Setter Methods for Instance Variables
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

    def build_search_query(self, inp_db: str = None, schema: str = None, table: str = None, column_name: str = None,
                           like_flag: bool = None, col_and_or: str = None):
        """
        Builds and returns a search query based on the specified parameters and instance variables.

        Parameters:
            inp_db (str, optional): The database to use (default is None).
            schema (str, optional): The schema to use (default is None).
            table (str, optional): The table to search (default is None).
            column_name (str, optional): The name of the column to search (default is None).
            like_flag (bool, optional): Whether to use the LIKE operator for search criteria (default is None).
            col_and_or (str, optional): The AND/OR operator to use between search criteria (default is None).
        """

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

    def snowflake_pull(self, query: str, username: str = None, warehouse: str = None, database: str = None,
                       role: str = None, sample_table: bool = False, sample_val: bool = False,
                       table_sample: dict = None, dtypes_conv=None):

        """
        Executes a query in Snowflake and returns the results as a Pandas DataFrame.

        Parameters:
            query (str): The SQL query to execute.
            username (str, optional): The Snowflake username to use. If not provided, uses the one set in the class
                                      constructor.
            warehouse (str, optional): The Snowflake warehouse to use. If not provided, uses the one set in the class
                                       constructor.
            database (str, optional): The Snowflake database to use. If not provided, uses the one set in the class
                                      constructor.
            role (str, optional): The Snowflake role to use. If not provided, uses the one set in the class constructor.
            sample_table (bool, optional): Whether to return only a sample of the result table. Defaults to False.
            sample_val (bool, optional): Whether to return only a sample of the result values. Defaults to False.
            table_sample (dict, optional): Dictionary containing the number of rows to return per table in the query.
                                           If not provided, returns all rows. Defaults to None.
            dtypes_conv (dict, optional): Dictionary containing the column names and their desired data types. If not
                                          provided, uses the default data types.

        Returns:
            pandas.DataFrame: The results of the query as a Pandas DataFrame.
        """

        # Set default values for the parameters if they are not provided
        if username is None:
            username = self.__username
        if warehouse is None:
            warehouse = self.__warehouse
        if database is None:
            database = self.__database
        if role is None:
            role = self.__role

        # Call the snowflake_pull method from the _SnowflakeData module using the provided or default parameters
        return _SnowflakeData.SnowflakeData.snowflake_pull(self, query, un=username, wh=warehouse, db=database,
                                                           role=role, sample_table=sample_table, sample_val=sample_val,
                                                           table_sample=table_sample, dtypes_conv=dtypes_conv)


