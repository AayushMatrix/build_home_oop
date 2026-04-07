from loguru import logger

class Labour:

    def __init__(self,first_name,last_name,wage):
        self.first = first_name
        self.last = last_name
        self.wage = wage 
       

    def save_to_databse(self,db_connection):
        query = "select id from labours where lower(first_name) = %s AND lower(last_name) = %s"
        result = self.crud.read_from_pos(query,(self.first_name,self.last_name))

        if result:
            logger.info(f"Labour already exixts with ID: {result[0][0]}")
            return result[0][0]
        # db_connection.save()

    def login(self):
        pass 



mansih = Labour("manish","kumar",500)
ram = Labour("Ram","Sing",400)
print(mansih._Labour__wage)
# print(ram.total_count)

 