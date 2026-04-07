from src.main.databases.postgre_connector import logger,PostgresConnection,PostgresCRUDOperation
from src.main.labours.labour_class import Labour


import configparser
config = configparser.ConfigParser()
config.read(r"C:\Users\Aayush-Gyawali\Desktop\python\src\resources\config_file.ini")


def main():
    # pos_db_connection = PostgresConnection(config)
    # pos_db_connection.connect() 

    # crud_operation_obj = PostgresCRUDOperation(pos_db_connection.connection)
    # final_result = crud_operation_obj.read_from_pos("select name from labours_table")

    # logger.info(f"{final_result}")
    
    # pos_db_connection.close()

    # query = "select * from labours_table"                    
    # final_result = read_from_postgres(config,query)
    # logger.info(f"{final_result}")

    postgre_db_conn_obj = PostgresConnection(config)
    postgre_db_conn_obj.connect()

    crud = PostgresCRUDOperation(postgre_db_conn_obj.connection)

    mansih_obj = Labour("Chabi","Bohara",100,"Mistri",crud)
    # mansih_obj.save_to_databse(crud)

    # ram_obj = Labour("Ram","Sing",400,"Mistri")
    
if __name__== "__main__":
    main()