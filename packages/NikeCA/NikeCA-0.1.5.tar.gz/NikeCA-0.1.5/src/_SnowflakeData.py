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

    def snowflake_pull(self, query: str, un, wh, db, role, schema=None, table=None, sample_table: bool = False,
                       sample_val: bool = False, table_sample: dict = None, dtypes_conv=None) -> pandas.DataFrame:

        """
        function: pulls snowflake data

        dependencies: [
            pandas,
            snowflake.connector,
            time,
            datetime.datetime
        ]

        :param table:
        :param schema:
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

        # try:
        cur.execute(query)  # execute sql, store into-->

        # except snowflake.connector.errors.ProgrammingError:
        #     print("Snowflake timed out and reached it's limit at 30 minutes")

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

    def search_schema(self, un, wh, db, role, sample_table: bool = False, sample_val: bool = False,
                      table_sample: dict = None, dtypes_conv=None, schema=None, table=None, column_name=None,
                      col_and_or='and', get_ex_val=False, like_flag=True):

        import pandas as pd

        # --> pull data, filter out exclusions
        results = pd.DataFrame()
        if type(db) == list:
            for d in db:
                temp_results = SnowflakeData.snowflake_pull(
                    self
                    , query=SnowflakeData.build_search_query(
                        self, inp_db=d, schema=schema, table=table, column_name=column_name, like_flag=like_flag,
                        col_and_or=col_and_or),
                    un=un, wh=wh, db=db, role=role, sample_table=sample_table,
                    sample_val=sample_val, table_sample=table_sample, dtypes_conv=dtypes_conv)
                results = pd.concat([results, temp_results], axis=0)
        elif db is None:
            # --> check user's database access for list of dbs to check
            get_dbs = SnowflakeData.snowflake_pull(self, query='''SHOW DATABASES''', un=un, db=db, wh=wh, role=role)

            # list of user's db names
            db_names = list(get_dbs['name'].values)

            print(f"No input database --> checking all of databases in user's access: {len(db_names)} total databases")
            for db in db_names:
                temp_results = SnowflakeData.snowflake_pull(
                    self,
                    query=SnowflakeData.build_search_query(self, inp_db=db, schema=schema, table=table,
                                                           column_name=column_name, like_flag=like_flag,
                                                           col_and_or=col_and_or),
                    un=un, db=db, wh=wh, role=role)
                results = pd.concat([results, temp_results], axis=0)
        else:
            results = SnowflakeData.snowflake_pull(
                self,
                query=SnowflakeData.build_search_query(self, inp_db=db, schema=schema, table=table,
                                                       column_name=column_name, like_flag=like_flag,
                                                       col_and_or=col_and_or),
                un=un, db=db, wh=wh, role=role)

        # exclude from table results
        exclusions = ['TEST', 'BACKUP', 'BKUP', 'BCKUP', 'BCKP', '_OLD', 'UPDT', 'DELETED', 'FIX']
        # drop exclusion rows
        results_fin = results[~results['TABLE_NAME'].str.contains('|'.join(exclusions))].copy().reset_index(drop=True)

        # --> print result statement
        print(f'''
    Total table-columns found: {len(results_fin)}    

    Unique column names found: {list(results_fin['COLUMN_NAME'].unique())}
    Total = {len(list(results_fin['COLUMN_NAME'].unique()))}
        ''')

        # --> flagged to retrieve a sample value for each column
        if get_ex_val:
            results_fin['EX_VALS'] = None
            # --> loop through each row & retrieve values
            for indx, row in results_fin.iterrows():
                try:
                    row_res = SnowflakeData.snowflake_pull(self, '', un=un, db=None, wh=wh, role=role, sample_val=True,
                                                           table_sample={'db': row['TABLE_CATALOG'],
                                                                         'schema': row['TABLE_SCHEMA'],
                                                                         'table': row['TABLE_NAME'],
                                                                         'col': row['COLUMN_NAME']})  # row results
                    # set row example values equal to unique column value list
                    row['EX_VALS'] = list(row_res[row['COLUMN_NAME']].unique())
                except:
                    print(f"Could not pull {row['COLUMN_NAME']} for table: {row['TABLE_NAME']}")
                    continue

        return results_fin
