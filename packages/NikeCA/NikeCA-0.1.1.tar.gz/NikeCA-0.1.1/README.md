# Nike CA

This package was developed informally for the Commercial Analytics Team at Nike

Before trying to use this package ensure that you have the proper access (This can be found under the "Usage" Section below)

This is a start to see about developing package to facilitate, standardize, and automate repetitive tasks

# Installation

Run the following to install:

```
$ python pip install NikeCA
```

# Usage

To use this package ensure that you have the following Snowflake Information:

* Username
* Warehouse Name
* Role Name

#### Dependencies:
* "wheel",
* "asn1crypto==1.5.1",
* "certifi==2022.12.7",
* "cffi==1.15.1",
* "charset-normalizer==2.1.1",
* "cryptography==39.0.1",
* "databricks==0.2",
* "databricks-sql==1.0.0",
* "databricks-sql-connector==2.2.1",
* "filelock==3.9.0",
* "gitdb==4.0.10",
* "GitPython==3.1.31",
* "greenlet==2.0.2",
* "idna==3.4",
* "lz4==4.3.2",
* "numpy==1.23.4",
* "oauthlib==3.2.2",
* "oscrypto==1.3.0",
* "pandas==1.5.3",
* "pyarrow==10.0.1",
* "pycparser==2.21",
* "pycryptodomex==3.17",
* "PyJWT==2.6.0",
* "pyOpenSSL==23.0.0",
* "pystache==0.6.0",
* "python-dateutil==2.8.2",
* "pytz==2022.7.1",
* "requests==2.28.2",
* "six==1.16.0",
* "smmap==5.0.0",
* "snowflake-connector-python==3.0.0",
* "snowflake-sqlalchemy==1.4.6",
* "SQLAlchemy==1.4.46",
* "thrift==0.16.0",
* "typing_extensions==4.5.0",
* "urllib3==1.26.14",
* "xcrun==0.4",
* "configparser~=5.3.0"

# Modules
* NikeSF
* NikeQA

# NikeSF Module
A Module for interacting with Snowflake databases and executing queries.

### Import

Run the following to import:

```
import NikeSF
```

## Classes:
* Snowflake()

### Snowflake()

#### Constructor:
    # Constructor
    def __init__(self, username: str, warehouse: str, role: str, database: str = None, schema: str = None,
                 table: str = None, column_name: str = None, col_and_or: str = 'AND', get_ex_val: bool = None,
                 like_flag: bool = False):
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

#### Parameters:
* username (str): The Snowflake account username


* warehouse (str): The Snowflake warehouse to use


* role (str): The Snowflake role to use


* database (str, optional, default=None): The Snowflake database to use


* schema (str, optional, default=None): The Snowflake schema to use


* table (str, optional, default=None): The Snowflake table to use


* column_name (str, optional, default=None): The name of the column to search


* col_and_or (str, optional, default=None): The AND/OR operator to use between search criteria


* get_ex_val (bool, optional, default=None): Whether to return exact matches only


* like_flag (bool, optional, default=None): Whether to use the LIKE operator for search criteria


## Methods:
* snowflake_pull(self, query: str, username: str = None, warehouse: str = None, database: str = None,
                       role: str = None, sample_table: bool = False, sample_val: bool = False,
                       table_sample: dict = None, dtypes_conv=None)


* build_search_query(self, inp_db: str = None, schema: str = None, table: str = None,
                           column_name=None, like_flag: bool = False, col_and_or: str = 'AND')

* search_schema(self, username=None, warehouse=None, database=None, role=None, sample_table: bool = False,
                      sample_val: bool = False, table_sample: dict = None, dtypes_conv=None, schema=None,
                      table=None, column_name=None, col_and_or='and', get_ex_val=False, like_flag=False)

#### snowflake_pull(self, query: str, username: str | None = None, warehouse: str | None = None, database: str | None = None, role: str | None = None, sample_table: bool = False, sample_val: bool = False, table_sample: dict | None = None, dtypes_conv: Any = None) -> DataFrame:

pulls snowflake data

#### Dependencies:
* pandas
* snowflake.connector

#### Parameters: 
* query (str): SQL query to run on Snowflake 
  * e.g. ```SELECT * FROM NGP_DA_PROD.POS.TO_DATE_AGG_CHANNEL_CY```


* username (str or None, default=None): Nike Snowflake Username 
  * e.g. "USERNAME"
  * notes
       ```
       if username is None:
            username = self.__username
       ```


* database (str or None, default=None): Name of the Database 
  * e.g. "NGP_DA_PROD"
  * notes
       ```
       if database is None:
            database = self.__database
       ```


* warehouse (str or None, default=None): Name of the Warehouse 
  * e.g. "DA_DSM_SCANALYTICS_REPORTING_PROD"
  * notes
       ```
       if warehouse is None:
            warehouse = self.__warehouse
       ```


* role (str or None, default=None): Name of the role under which you are running Snowflake 
  * e.g. "DF_*****"
  * notes
       ```
       if role is None:
            role = self.__role
       ```


* sample_table (bool, optional, Default=False): pull only 500 records from table


* sample_val (bool, optional, default=False)


* table_sample (dictionary, optional, default=None) 
  * Notes: The below code is built within the Module
    ``` 
    if table_sample is not None: 
         table_sample = {'db': None, 'schema': None, 'table': None, 'col': None}
    ```


* dtypes_conv (any, default=None)


#### return:
* pandas.DataFrame

Run the following in python to generate a sample query:



```
from NikeSF import Snowflake

username = <Your Username>
warehouse = <The Name of the Warehouse>
role = <Name of Your Role>
database = <Name of the Database>

sf =  Snowflake(username=username, warehouse=warehouse, role=role, database=database)

query = 'SELECT TOP 2 * FROM  NGP_DA_PROD.POS.TO_DATE_AGG_CHANNEL_CY'

print(sf.snowflake_pull(query)) 
```

#

---
#
### build_search_query(self, inp_db: str | None = None, schema: str | None = None, table: str | None = None, column_name=None, like_flag: bool = False, col_and_or: str = 'AND') -> str:

Builds and returns a search query based on the specified parameters and instance variables

#### Dependencies:
None

#### Parameters: 
* inp_db (str or None, optional, default=None): The database name to search in. If not specified, search all databases
  

* schema (str or None, optional, default=None): The schema name to search in. If not specified, search all schemas
  * Notes
    ```
    if schema is None:
         schema = self.__schema
    ```

* table (str or None, optional, default=None): The table name to search for. If not specified, search all tables
  * Notes
    ```
    if table is None:
         table = self.__table
    ```


* column_name(any, optional, default=None): The column name(s) to search for. If not specified, search all columns
  * If a list is provided, search for any columns that match any of the names in the list
  * Notes
    ```
    if column_name is None:
         column_name = self.__column_name
    ```


* like_flag (bool, optional, default=False) 
  * If True, uses a SQL LIKE statement to search for columns that contain the specified column name(s)
    ```
    f"AND column_name like '{column_name}' " if like_flag else where_stmt + f"AND column_name = '{column_name}' "
    ```
  * If False, searches for exact matches to the specified column name(s)
    ```
    f"AND column_name like '{column_name}' " if like_flag else where_stmt + f"AND column_name = '{column_name}' "
    ```
  * Notes
    ```
    if (not like_flag) and self.like_flag:
         like_flag = self.__like_flag
    ```
    

* col_and_or (str: optional, default='AND'): If specified and column_name is a list, determines whether to search for columns that match all or any of 
the names in the list. Must be one of the following values: 'AND', 'and', 'OR', 'or'.
  * Notes
    ```
    if col_and_or.lower() == 'and' and self.__col_and_or:
         col_and_or = self.__col_and_or
    ```
 


#### return: 
* string of the SQL Statement

#### Run the following in python to generate a sample query
```
from NikeSF import Snowflake

username = <Your Username>
warehouse = <The Name of the Warehouse>
role = <Name of Your Role>
database = <Name of the Database>

sf = Snowflake(username=username, warehouse=warehouse, role=role, database=database)

print(sf.build_search_query(column_name='%DISTINCT%', like_flag=True))
```

#

---
#

#### the build_search_query() and the snowflake_pull() methods may be combined
```
from NikeQA import QA
from NikeSF import Snowflake

username = <Your Username>
warehouse = <The Name of the Warehouse>
role = <Name of Your Role>
database = <Name of the Database>

sf = Snowflake(username=username, warehouse=warehouse, role=role, database=database)

print(sf.snowflake_pull(sf.build_search_query(column_name='%DISTINCT%', schema='EIS', like_flag=True)))
```

#### search_schema(self, username=None, warehouse=None, database=None, role=None, sample_table: bool = False, sample_val: bool = False, table_sample: dict = None, dtypes_conv=None, schema=None, table=None, column_name=None, col_and_or='and', get_ex_val=False, like_flag=False)

Search snowflake structure for specific schemas/tables/columns

Will allow to search for tables/cols/etc. even without knowing the db if database=None

#### Dependencies:
* pandas
* snowflake.connector

#### Parameters:

* username (str or None, default=None): Nike Snowflake Username 
  * e.g. "USERNAME"
  * notes
       ```
       if username is None:
            username = self.__username
       ```
* database (str or None, default=None): Name of the Database 
  * e.g. "NGP_DA_PROD"
  * notes
       ```
       if database is None:
            database = self.__database
       ```


* warehouse (str or None, default=None): Name of the Warehouse 
  * e.g. "DA_DSM_SCANALYTICS_REPORTING_PROD"
  * notes
       ```
       if warehouse is None:
            warehouse = self.__warehouse
       ```


* role (str or None, default=None): Name of the role under which you are running Snowflake 
  * e.g. "DF_*****"
  * notes
       ```
       if role is None:
            role = self.__role
       ```


* sample_table (bool, optional, Default=False): pull only 500 records from table

        if not sample_table and self.__sample_table:
            sample_table = self.__sample_table

* sample_val (bool, optional, default=False)

        if not sample_val and self.__sample_val:
            sample_val = self.__sample_val

* table_sample (dictionary, optional, default=None) 
  * Notes: The below code is built within the Module

  
        if table_sample is None and self.__table_sample:
            table_sample = self.__table_sample
        if table_sample is not None: 
             table_sample = {'db': None, 'schema': None, 'table': None, 'col': None}

* dtypes_conv (any, default=None)

        if dtypes_conv is None and self.__dtypes_conv:
            dtypes_conv = self.__dtypes_conv
* schema (str, default=None): Snowflake schema name from any database 

        if schema is None and self.__schema:
            schema = self.__schema

* table (str, default=None): Snowflake table name

        if table is None and self.__table:
            table = self.__table

* column_name (str, default=None): column name to filter

        if column_name is None and self.__column_name:
            column_name = self.__column_name

* col_and_or (str, default='and'): either 'and' or 'or'
  * will use in the where statement

        if col_and_or == 'and' and self.__col_and_or:
            col_and_or = self.__col_and_or

* get_ex_val (bool, default=False)

        if not get_ex_val and self.__get_ex_val:
            get_ex_val = self.__get_ex_val

* like_flag (bool, default=False): This signifies whether the "column_name like " or "column_name = "

        if not like_flag and self.__like_flag:
            like_flag = self.__like_flag

#### return:

* Dataframe

Run the following in python to generate a sample table:

    from NikeSF import Snowflake
    
    sf = Snowflake(username=<your username>, warehouse=<your warehouse>, 
         role=<your role>, database=<database you would like to search or none>)
    
    sf.column_name = '%DISCOUNT%'
    sf.schema = 'POS'
    sf.like_flag = True
    
    print(sf.search_schema())

#

---


---
#
# NikeQA Module
A Module for interacting with the data and doing basic QA

### Import

Run the following to import:

```
import NikeQA
```

## Classes:
* QA()

### QA():

#### Constructor:
    def __init__(self, df: pd.DataFrame, df2: pd.DataFrame = None, ds1_nm: str = 'Source #1', ds2_nm: str = 'Source #2',
                 case_sens: bool = True, print_analysis: bool = True, check_match_by=None, breakdown_grain=None):
        self.__df = df
        self.__df2 = df2
        self.__ds1_nm = ds1_nm
        self.__ds2_nm = ds2_nm
        self.__case_sens = case_sens
        self.__print_analysis = print_analysis
        self.__check_match_by = check_match_by
        self.__breakdown_grain = breakdown_grain

#### Parameters:
* df (DataFrame)


* df2 (DataFrame, optional, default=None)


* ds1_nm (str, optional, default='Source #1')


* ds2_nm (str, optional, default='Source #2')


* case_sens (bool, optional, default=True)


* print_analysis (bool, optional, default=True)


* check_match_by (any, optional, default=None)


* breakdown_grain (any, optional, default=None)

## Methods:
* column_gap_analysis(self, df2: pd.DataFrame = None, ds1_nm: str = 'Source #1',  ds2_nm: str = 'Source #2', 
case_sens: bool = True, print_analysis: bool = True, check_match_by=None, breakdown_grain=None, df=None)

### column_gap_analysis(self, df2: pd.DataFrame = None, ds1_nm: str = 'Source #1', ds2_nm: str = 'Source #2', case_sens: bool = True, print_analysis: bool = True, check_match_by=None, breakdown_grain=None, df=None)
Compares 2 DataFrames and gives shape, size, matching columns, non-matching columns, coverages, and percentages
#### Dependencies:
* "pandas==1.5.3",

#### Parameters: 
* df (DataFrame)
  * Notes

        if df is None:
              df = self.__df

* df2 (DataFrame, optional, default=None)
  * Notes

        if df2 is None:
            df2 = self.__df2
        if df2 is None:
            raise ValueError(f'Please insert pandas.DataFrame for df2')


* ds1_nm (str, optional, default='Source #1')
  * Notes

        if ds1_nm == 'Source #1':
            ds1_nm = self.__ds1_nm


* ds2_nm (str, optional, default='Source #2')
  * Notes

        if ds2_nm == 'Source #2':
            ds2_nm = self.__ds2_nm


* case_sens (bool, optional, default=True)
  * Notes

        if case_sens:
            case_sens = self.__case_sens


* print_analysis (bool, optional, default=True)
  * Notes

        if print_analysis:
            print_analysis = self.__print_analysis


* check_match_by (any, optional, default=None)
  * Notes

        if check_match_by is None:
            check_match_by = self.__check_match_by


* breakdown_grain (any, optional, default=None)
  * Notes

        if breakdown_grain is None:
            breakdown_grain = self.__breakdown_grain


#### return: 
* DataFrame

#### Run the following in python to generate a sample query
```
from NikeQA import QA
from NikeSF import Snowflake

username = <Your Username>
warehouse = <The Name of the Warehouse>
role = <Name of Your Role>
database = <Name of the Database>

sf = Snowflake(username=username, warehouse=warehouse, role=role, database=database)

df = sf.snowflake_pull(sf.build_search_query(column_name='%DISTINCT%', like_flag=True))[['TABLE_CATALOG', 'TABLE_SCHEMA', 'COLUMN_NAME']]

df2 = sf.snowflake_pull(sf.build_search_query(column_name='%DISTINCT%', schema='EIS', like_flag=True))

qa = QA(df=df, df2=df2)
print(qa.column_gap_analysis())
```