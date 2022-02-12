import pyodbc
import Config


class Repository:
    def __init__(self):
        self.sql_get_data = "EXEC [dbname].[schema].[stored-procedure-name]"
        self.__config = config.Config()
        self.__connection_string = r'DRIVER={SQL Server};SERVER=' + self.__config.__sql_server + \
        ';DATABASE=' + self.__config.sql_database + \
        ';UID=' + self.__config.sql_user +\
        ';PWD=' + self.__config.sql_pass
    self.columns = []

    def get_data(self):
        conn = pyodbc.connect(self.__connection_string, autocommit=True)
        cursor = conn.cursor()
        cursor.execute(self.sql_get_data)

        rows = cursor.fetchall()
        self.columns = [column[0] for column in cursor.description]
        conn.close()
        return rows