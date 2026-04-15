from datetime import datetime
from src.main.models.person import Person,logger

class AttendanceServices:
    def __init__(self,db_connection):
        self.db_connection = db_connection

    def login_logout(crud, id=None, first_name=None, last_name=None):
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


