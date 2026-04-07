from loguru import logger

class Labour:
    def __init__(self,first_name,last_name,wage,role,crud):
        self.first_name = first_name
        self.last_name = last_name
        self.wage = wage 
        self.role = role
        self.crud = crud
        self.__save_to_databse(self.crud)
      
       

    def __save_to_databse(self,crud):
        query = "select id from labours where lower(first_name) = %s AND lower(last_name) = %s"
        result = crud.read_from_pos(query,(self.first_name.lower(),self.last_name.lower()))

        if result:
            logger.info(f"Labour already exixts with ID: {result[0][0]}")
            return result[0][0]
        
        insert_query = """INSERT INTO labours (first_name, last_name,wage,role,email)
                         VALUES(%s,%s,%s,%s,%s)
        RETURNING id
        """
        email = self.first_name + "." + self.last_name + "@gmail.com"
        
        insert_result = crud.insert_from_pos(insert_query,(self.first_name,self.last_name,self.wage,self.role,email))
        
        # new_id = insert_result[0][0]
        # logger.info(f"New labour added with ID: {new_id}")
        # return new_id

        logger.info(f"New labour added with ID: {insert_result[0][0]}")
        return insert_result[0][0]
        # db_connection.save()

    def login(self):
        pass 



# config = configparser.ConfigParser()
# config.read(r"C:\Users\Aayush-Gyawali\Desktop\python\src\resources\config_file.ini")

# postgre_db_conn_obj = PostgresConnection(config)
# postgre_db_conn_obj.connect()

# crud = PostgresCRUDOperation(postgre_db_conn_obj.connection)

# mansih_obj = Labour("manish","kumar",500)
# mansih_obj.save_to_databse(crud)

# ram = Labour("Ram","Sing",400)
# print(mansih._Labour__wage)
# print(ram.total_count)