from datetime import datetime
from src.main.databases.postgre_connector import PostgresCRUDOperation
from loguru import logger

class AttendanceServices:

    def __init__(self, db_connection):
        self.crud = PostgresCRUDOperation(db_connection)

    def login_logout(self, labour_id=None, first_name=None, last_name=None):
        try:
          
            if labour_id is None:
                if not first_name or not last_name:
                    logger.error("Provide either labour_id or name")
                    return

                query = """
                SELECT id FROM labours
                WHERE lower(first_name) = %s
                AND lower(last_name) = %s
                """

                result = self.crud.read_from_pos(query,(first_name.lower(), last_name.lower()))

                if not result:
                    logger.error("Labour not found. Register first.")
                    return

                labour_id = result[0][0]
                logger.info(f"Labour ID: {labour_id}")

            current_time = datetime.now()
            current_date = current_time.date()

         
            check_query = """
            SELECT id, start_time, end_time FROM attendance
            WHERE labour_id = %s AND DATE(start_time) = %s
            """

            result = self.crud.read_from_pos(check_query, (labour_id, current_date))

            if not result:
                # LOGIN
                insert_query = """
                INSERT INTO attendance (labour_id, start_time)
                VALUES (%s, %s)
                """
                self.crud.insert_from_pos(insert_query, (labour_id, current_time))
                logger.info(f"Labour {labour_id} logged IN at {current_time}")

            else:
                attendance_id = result[0][0]

                # LOGOUT
                update_query = """
                UPDATE attendance
                SET end_time = %s
                WHERE id = %s
                """
                self.crud.insert_from_pos(update_query, (current_time, attendance_id))
                logger.info(f"Labour {labour_id} logged OUT at {current_time}")

        except Exception as e:
            logger.error(f"Error in login_logout: {e}")