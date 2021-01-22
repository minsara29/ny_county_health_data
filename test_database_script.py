from unittest.mock import MagicMock,Mock
from unittest import TestCase
from database_script import SqliteDb
import sqlite3

class TestDatabase(TestCase):

    def setUp(self):
        self.db = SqliteDb()


    def test_sqlite3_connect_success(self):

        sqlite3.connect = MagicMock(return_value='connection succeeded')

        dbc = SqliteDb()
        sqlite3.connect.assert_called_with('file::memory:?cache=shared', uri=True)
        self.assertEqual(dbc.db_conn(),'connection succeeded')



    def tearDown(self):
        pass
        # TODO: clean up your test