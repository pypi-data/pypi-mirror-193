
class SnowflakeData:

    import pandas

    def build_search_query(self, inp_db=None, schema=None, table=None, column_name=None, like_flag=False,
                           col_and_or='AND'):
        """
        Constructs a SQL query for searching tables and columns in a database based on specified search criteria.

        Parameters:
        -----------
        inp_db: str, optional
            The database name to search in. If not specified, searches all databases.
        schema: str, optional
            The schema name to search in. If not specified, searches all schemas.
        table: str, optional
            The table name to search for. If not specified, searches all tables.
        column_name: str or list of str, optional
            The column name(s) to search for. If not specified, searches all columns.
            If a list is provided, searches for any columns that match any of the names in the list.
        like_flag: bool, optional
            If True, uses a SQL LIKE statement to search for columns that contain the specified column name(s).
            If False, searches for exact matches to the specified column name(s).
            If not specified, defaults to False.
        col_and_or: str, optional
            If specified and column_name is a list, determines whether to search for columns that match all or any of
            the names in the list. Must be one of the following values: 'AND', 'and', 'OR', 'or'.
            If not specified, defaults to 'AND'.

        Returns:
        --------
        str
            The constructed SQL query string.
        """

        # ie. always TRUE --> allows us to search for tables/cols/etc. even without knowing the db
        where_stmt = "WHERE 1=1 "
        where_stmt = where_stmt + f"AND table_catalog = '{inp_db}' " if inp_db else where_stmt
        where_stmt = where_stmt + f"AND table_schema = '{schema}' " if schema else where_stmt
        where_stmt = where_stmt + f"AND table_name = '{table}' " if table else where_stmt

        # add column(s) search criteria -->
        # if like_flag = false then column name equals
        # if column_name is a list add an AND statement for each search value in the list
        if column_name is not None:
            if type(column_name) == str:
                where_stmt = where_stmt + f"AND column_name like '{column_name}' " \
                    if like_flag else where_stmt + f"AND column_name = '{column_name}' "

            # OR statement where value matches multiple
            elif (type(column_name) == list) & (not like_flag):
                where_stmt = where_stmt + f"""AND column_name in ({' ,'.join(f"'{str(x)}'" for x in column_name)})"""

            # --> user input list of search criteria
            elif type(column_name) == list:
                for idx, x in enumerate(column_name):

                    # col contains all column_name search criteria
                    if col_and_or.lower() == 'and':
                        where_stmt = where_stmt + f"AND column_name like '{x}' " \
                            if like_flag else where_stmt + f"AND column_name = '{x}' "

                    # col contains any of the column_name search criteria
                    elif col_and_or.lower() == 'or':
                        where_stmt = where_stmt + f"AND (column_name like '{x}' " \
                            if idx == 0 else where_stmt + f"OR column_name like '{x}' "

                    # non-matching input value
                    else:
                        raise ValueError('col_and_or input must match: AND/And/and, OR/Or/or')
                where_stmt = where_stmt + ')' if (type(column_name) == list) & (col_and_or == 'or') else where_stmt

            # --> invalid format
            else:
                raise ValueError(f'ERROR: column_name={column_name} does not match required input of list/string')

        # final search-schema query
        query = f'''        
        SELECT 
            DISTINCT
            TABLE_CATALOG
            ,TABLE_SCHEMA
            ,TABLE_NAME
            ,COLUMN_NAME
            ,IS_NULLABLE
            ,DATA_TYPE
        FROM 
            INFORMATION_SCHEMA.COLUMNS
        {where_stmt}
        ORDER BY 
            TABLE_CATALOG
            , TABLE_SCHEMA
            , TABLE_NAME
            , COLUMN_NAME
        '''

        return query

    def snowflake_pull(self, query: str, un, wh, db, role, sample_table: bool = False, sample_val: bool = False,
                       table_sample: dict = None, dtypes_conv=None) -> pandas.DataFrame:

        """
        function: pulls snowflake data

        dependencies: [
            pandas,
            snowflake.connector,
            time,
            datetime.datetime
        ]

        :param query: str
            SQL query to run on Snowflake
            query = "SELECT * FROM  NGP_DA_PROD.POS.TO_DATE_AGG_CHANNEL_CY"

        :param un: str
            Nike Snowflake Username
                "USERNAME"

        :param db: str, default 'NA'
            Name of the Database

        :param wh: str
            Name of the Wharehouse
            e.g. "DA_DSM_SCANALYTICS_REPORTING_PROD"

        :param role: str
            Name of the role under which you are running Snowflake
                "DF_######"

        :param sample_table: bool, default: False

        :param sample_val: bool, default: False

        :param table_sample: dict, default: None
            later
                if table_sample = None
                    table_sample = {'db': None, 'schema': None, 'table': None, 'col': None}

        :param dtypes_conv: default: None

        :return: pandas.DataFrame
        """

        # snowflake connection packages:
        import pandas as pd
        import snowflake.connector

        if table_sample is not None:
            table_sample = {'db': None, 'schema': None, 'table': None, 'col': None}

        # --> take a random sample from a table in snowflake
        query = f'''SELECT * FROM {table_sample['db']}.{table_sample['schema']}.{table_sample['table']} LIMIT 100''' \
            if sample_table else query

        # --> take a random sample of a column from a table in snowflake
        query = f'''SELECT DISTINCT 
                {table_sample['col']} 
            FROM 
                {table_sample['db']}.{table_sample['schema']}.{table_sample['table']} 
            ORDER BY 1 LIMIT 10''' \
            if sample_val else query

        # connection settings
        conn = snowflake.connector.connect(
            user=un,
            account='nike',

            # opens separate browser window to confirm authentication
            authenticator='externalbrowser',
            warehouse=wh,
            database=db,
            role=role
        )

        # connect to snowflake using conn variables
        cur = conn.cursor()
        cur.execute(query)  # execute sql, store into-->

        try:
            # final data pull --> allows datatype-memory optimization
            df = cur.fetch_pandas_all() if dtypes_conv is None else cur.fetch_pandas_all().astype(
                dtypes_conv)

        # --> allows metadata querying
        except:
            temp_df = cur.fetchall()  # return data
            cols = [x.name for x in cur.description]  # get column names
            df = pd.DataFrame(temp_df, columns=cols)  # create dataset

        conn.close()
        cur.close()
        return df




