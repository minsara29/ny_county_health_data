import sqlite3

TABLE_CREATE_STATEMENT = 'CREATE TABLE IF NOT EXISTS '
TABLE_COLUMNS_STATEMENT = """(
        Test_Date datetime, 
        New_Positives NUM,
        Cumulative_Number_of_Positives NUM, 
        Total_Number_of_Tests_Performed NUM,
        Cumulative_Number_of_Tests_Performed NUM,
        Load_date date default CURRENT_DATE
    );"""

TABLE_INSERT_STATEMENT = 'INSERT INTO '
TABLE_COLUMNS_VALUES = """(
        Test_Date, 
        New_Positives, 
        Cumulative_Number_of_Positives, 
        Total_Number_of_Tests_Performed, 
        Cumulative_Number_of_Tests_Performed)
    VALUES (?, ?, ?, ?, ?);
"""


class SqliteDb:
    """

    SQLite database connection, table creation, insert and select query for county

    """

    def __init__(self):
        self.db = self.db_conn()

    def db_conn(self):
        """ Open the DB connection. """
        try:
            return sqlite3.connect("file::memory:?cache=shared", uri=True)
        except sqlite3.Error as e:
            print(f"Error while connecting to SQLite : {e}")
            raise SystemExit(e)

    def create_table(self, county):
        """ Create a County table. """
        county = str(county).replace(".", "").replace(" ", "_")
        create_table = TABLE_CREATE_STATEMENT + county + TABLE_COLUMNS_STATEMENT

        try:
            return self.db.execute(create_table)
        except sqlite3.Error as e:
            print(f"Error while creating {county} table: {e}")
            raise SystemExit(e)

    def insert_data(self, county, values):
        """ Insert values into County table. """
        county = str(county).replace(".", "").replace(" ", "_")
        insert_query = TABLE_INSERT_STATEMENT + county + TABLE_COLUMNS_VALUES
        cur = self.db.cursor()
        try:
            for value in values:
                cur.execute(insert_query, (value))
        except sqlite3.Error as e:
            print(f"Error while inserting {county} table: {e}")
            raise SystemExit(e)

        self.db.commit()

    def select_data(self, county):
        """ select rows from County table. """
        county = str(county).replace(".", "").replace(" ", "_")
        select_query = f"select * from {county}"
        cur = self.db.cursor()
        try:
            cur.execute(select_query)
            return cur.fetchall()
        except sqlite3.Error as e:
            print(f"Error while selecting {county} table: {e}")
            raise SystemExit(e)
