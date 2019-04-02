# ----------------------------------------------------------------------------------------------------------------------
# database access to test project mysql-log-analysis-ELK

# database class
from mysql.connector import errorcode
import mysql.connector


class Database:
    def __init__(self, host, port, database, user, password):
        try:
            self.conn = mysql.connector.connect(host=host,
                                                port=port,
                                                database=database,
                                                user=user,
                                                password=password)
            self.is_connected = True
            self.last_error_code = 0
            self.last_error_msg = ''
        except mysql.connector.Error as err:
            self.is_connected = False
            self.conn = None
            self.cursor = None
            self.last_error_code = err.errno
            self.last_error_msg = err.msg

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.is_connected = False
        try:
            self.conn.close()

        except mysql.connector.Error as err:
            self.last_error_code = err

    def execute_sp(self, sp, params):
        try:
            self.last_error_code = 0
            self.last_error_msg = ''
            self.cursor = self.conn.cursor()
            self.cursor.callproc(sp, params)
            self.conn.commit()

        except mysql.connector.Error as err:
            self.last_error_code = err.errno
            self.last_error_msg = err.msg

        finally:
            self.cursor.close()
            return None




