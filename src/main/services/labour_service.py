from src.main.databases.postgre_connector import PostgresCRUDOperation
from loguru import logger
from fastapi import HTTPException
class LabourServices:

    def __init__(self, db_connection):
        self.crud = PostgresCRUDOperation(db_connection)

    def create_labour(self, labour):

        check_query = """
        SELECT id FROM labours
        WHERE lower(first_name) = %s
        AND lower(last_name) = %s
        """

        result = self.crud.read_from_pos(
            check_query,
            (labour.first_name.lower(), labour.last_name.lower())
        )

        if result:
            raise ValueError(f"User already exists with ID {result[0][0]}")
            # return result[0][0]
            # return {"message": "User already exists", "id": result[0][0]}

        insert_query = """
        INSERT INTO labours(first_name, last_name, wage, role, email)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id
        """

        result = self.crud.insert_from_pos(
            insert_query,
            (
                labour.first_name,
                labour.last_name,
                labour.wage,
                labour.role,
                labour.email
            )
        )
        logger.info(f"Query:- {insert_query} values:- {result}")
        labbour_id =  result[0][0]

    
        if hasattr(labour,'skill') and labour.skill:
            skill_query = """INSERT INTO skills(labour_id,skill)
            VALUES (%s,%s)"""
            
            for skill in labour.skill:
                self.crud.insert_from_pos(skill_query,(labbour_id,skill))
                
        return labbour_id

    def get_labour(self, labour_id):

            check_query = """
            SELECT * FROM labours
            WHERE id = %s
            """    
            result = self.crud.read_from_pos(check_query,([labour_id]))
        
            if not result:
                # return result[0][0]
                raise HTTPException(status_code=404,detail="User Not Found ")

            row = result[0]
            return {
                "id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "wage": row[3],
                "role": row[4],
                "email": row[5]
            }

    def get_all_labour(self):

            check_query = """
            SELECT * FROM labours
            """    
            result = self.crud.read_from_pos(check_query)
        
            if not result:
                # return result[0][0]
                raise HTTPException(status_code=404,detail="User Not Found ")

            data = []
            for row in result:
                 data.append({
                "id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "wage": row[3],
                "role": row[4],
                "email": row[5]  
                 })

            return data