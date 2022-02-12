import os

class Config:
    def __init__(self):
        self.__sql_server = 'servername'
        self.__sql_database = 'dbname'
        self.__sql_user = 'sqlusername'
        self.__sql_pass = 'sqlpassword'
        self.path = 'C:\\Users\\user\\path'

        self.__sftp_hostname = "sftphostname"
        self.__sftp_username = "sftpusername"
        self.__sftp_pkPath = 'C:\\Users\\User\\pathToThePemFile'

    @property
    def sql_server(self):
        return self.__sql_server

    @property
    def sql_database(self):
        return self.__sql_database

    @property
    def sql_user(self):
        return self.__sql_user

    @property
    def sql_pass(self):
        return self.__sql_pass

    @property
    def sftp_host(self):
        return self.__sftp_hostname

    @property
    def ftp_user(self):
        return self.__sftp_username

    @property
    def sftp_pkPath(self):
        return self.__sftp_pkPath