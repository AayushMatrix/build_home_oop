from src.main.models.person import Person,logger

class LabourServices:
    def __init__(self,db_connection):
            self.db_connection = db_connection 

    def create_labour(self,crud,labour):
          cursor = self.db_connection.cursor()
          insert_query = """INSERT INTO labours(first_name,last_name,wage,role,email)
                     values (%s,%s,%s,%s,%s)
                    """
          crud.insert_from_pos(insert_query,(labour.first_name,labour.last_name,labour.wage,labour.role,labour.email))
