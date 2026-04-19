from src.main.databases.postgre_connector import PostgresCRUDOperation
from loguru import logger
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
            logger.info("User already exists")
            return result[0][0]

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

        return result[0][0]