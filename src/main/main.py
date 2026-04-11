from src.main.databases.postgre_connector import logger,PostgresConnection,PostgresCRUDOperation
from src.main.labours.labour_class import Labour,Person, Mistri


import configparser
config = configparser.ConfigParser()
config.read(r"C:\Users\Aayush-Gyawali\Desktop\python\src\resources\config_file.ini")


def main():

    postgre_db_conn_obj = PostgresConnection(config)
    postgre_db_conn_obj.connect()

    crud = PostgresCRUDOperation(postgre_db_conn_obj.connection)

    mistri_obj = Mistri("Ram","Lal",1000,"mistri",["Plumbing","painter"],crud)
    
if __name__== "__main__":
    main()