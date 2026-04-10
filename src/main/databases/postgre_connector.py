from loguru import logger 
import psycopg2
import psycopg2.extras


conn = None

class PostgresConnection:
    def __init__(self,config):
          self.config = config
          self.connection = None 

    def connect(self):
        try:     
            self.connection = psycopg2.connect(host = self.config["postgres_database"]["host"],
                dbname = self.config["postgres_database"]["database"],
                user = self.config["postgres_database"]["username"],
                password =self.config["postgres_database"]["pwd"],
                port = self.config["postgres_database"]["port_id"])
            logger.info("Postgres Connection succesful")
 
        except Exception as e:
              logger.error(f"Error occured: {e}")
              raise e
    
    def close(self):
        if self.connection is not None:
             self.connection.close()   
             self.connection = None   
             logger.info("Postgres Connection Close")   

        
class PostgresCRUDOperation:
    def __init__(self,postgre_connection):
        self.connection = postgre_connection 

    def read_from_pos(self,query, params = None):
        try:
              with self.connection.cursor() as cursor:
                    if params:
                         logger.info(f"Query sent to read\n{cursor.mogrify(query,params).decode('utf-8')}")
                         cursor.execute(query,params)
                    else:
                         cursor.execute(query)
                         
                    return cursor.fetchall()      

        except Exception as error:
            logger.info(f"Error occured in postgres query run  {error}")
            raise error
             

    def insert_from_pos(self, query,params = None):
        try:
            with self.connection.cursor() as cursor:
                if params:
                    cursor.execute(query,params)
                else:
                    cursor.execute(query)

                if "RETURNING" in query.upper():
                     result = cursor.fetchall()
                else:
                     result = None

                self.connection.commit()        
                logger.info("Insert successful") 
                return result
        
        except Exception as error:
            self.connection.rollback()      
            logger.info(f"Error occurred in postgres query run {error}")
            raise error



# def read_from_postgres(config,query):  
#     try:

        
#             logger.info(f"{conn}")
        
#             with conn.cursor() as cursor:
#                     # cursor.execute('DROP TABLE IF EXISTS EMPLOYEE')
#                     # insert_script = 'INSERT INTO employee (colum,name) values (%s,%s)'
#                     # insert_value = [(1,'Ram'),(1,'Ram'),(1,'Ram')]

#                     # for record in insert_values:
#                     #      cur.execute(insert_script,record)

#                     # insert_query = "INSERT INTO labours_table (name, role, wages) VALUES (%s, %s, %s)"
#                     # cursor.execute(insert_query, ('Rahul', 'labour', 700))

#                     cursor.execute(query)
#                     result = cursor.fetchall()
                    
#                     # logger.info(f"{result}")
#                     return result
            
#                     # for record in cursor.fetchall():
#                         # logger.info(f"{record['name']} ,{record['role']} ,{record['wages']}")
#                     # print(cursor.fetchall())

#                     # conn.commit()

#                     # cur.excute(insert_script,insert_value)


#     except Exception as error:
#         logger.info(f"{error}")
#         raise error

#     finally:
#             # cursor.close()          