from loguru import logger
from datetime import datetime



class Person:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.email = self.first_name + "." + self.last_name + "@gmail.com"

    def print_detail(self):
        return f"Your first name is set as {self.first_name} and last name is {self.last_name} with email id as {self.email}"

class Labour(Person):
    def __init__(self,first_name,last_name,wage,role,crud):
        super().__init__(first_name,last_name)
        self.wage = wage 
        self.role = role
        self.crud = crud
        self.id = self.__save_to_databse(self.crud)    
       

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

        insert_result = crud.insert_from_pos(insert_query,(self.first_name,self.last_name,self.wage,self.role,self.email))
        
        # new_id = insert_result[0][0]
        # logger.info(f"New labour added with ID: {new_id}")
        # return new_id

        logger.info(f"New labour added with ID: {insert_result[0][0]}")
        return insert_result[0][0]
        # db_connection.save()

    @staticmethod
    def login_and_logout(crud, id=None, first_name=None, last_name=None):
        try:
            if id is None:
                if first_name is None or last_name is None:
                    logger.error("Please provide either id or first name and last name")
                    return
                
                query = """
                        SELECT id FROM labours
                        WHERE lower(first_name) = %s
                        AND lower(last_name) = %s
                        """
                result = crud.read_from_pos(query, (first_name.lower(), last_name.lower()))
                
                if not result:
                    logger.error("Labour is not present. Please register first")
                    return
                
                id = result[0][0]
                logger.info(f"Id from labours table {id}")

            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            current_date = datetime.now().strftime('%Y-%m-%d')

            check_query = """
                            SELECT id, start_time, end_time FROM attendance
                            WHERE labour_id = %s AND DATE(start_time) = %s
                        """
            
            result = crud.read_from_pos(check_query, (id, current_date))
            logger.info(f"Data from attendance table {result}")

            if len(result)==0:
                insert_query = f""" 
                    INSERT INTO attendance (labour_id,start_time)
                    VALUES (%s,%s)
                """
                crud.insert_from_pos(insert_query,(id,current_time))
                logger.info(f"Labour {id} logged in at {current_time}")

            else:
                id = result[0][0]
                update_query = f"""
                                UPDATE attendance 
                                SET end_time = %s
                                WHERE id = %s
                                 """
                crud.insert_from_pos(update_query,(current_time,id))
                logger.info(f"Labour {id} logged out at {current_time}")

        except Exception as e:
            logger.error(f"Error in login_and_logout: {e}")

class Mistri(Labour):
    def __init__(self, first_name, last_name, wage, role,skill, crud):
        super().__init__(first_name, last_name, wage, role, crud)
        self.skill = skill
        self.__save_to_skill_table()

    def __save_to_skill_table(self):
        insert_query = """ INSERT INTO skills(labour_id,skill)
                           VALUES(%s,%s)
                         """
        for skill in self.skill:
            self.crud.insert_from_pos(insert_query,(self.id,skill))
            logger.info(f"Skill '{skill}' saved for labour ID {self.id}")