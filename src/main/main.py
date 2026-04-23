from src.main.databases.postgre_connector import logger,PostgresConnection,PostgresCRUDOperation
# from src.main.labours.labour_class import Labour,Person, Mistri
from src.main.factories.person_factory import PersonFactory
from src.main.services.attendance_service import AttendanceServices
from src.main.services.labour_service import LabourServices
from fastapi import FastAPI


import configparser
config = configparser.ConfigParser()
config.read(r"C:\Users\Aayush-Gyawali\Desktop\python\src\resources\config_file.ini")


db = PostgresConnection.get_instance(config)

app = FastAPI()


@app.post("/postcreateUser")
def create_user(first_name, last_name, wage, role):
    try:
        labour = PersonFactory.create_person(
            role,
            first_name=first_name,
            last_name=last_name,
            wage=wage,
            role=role
        )
        labour_service = LabourServices(db.connection)
        labour_id = labour_service.create_labour(labour)
        return {"status":"Sucess","message":f"User created with ID {labour_id}"}
    
    except Exception as e:
        return {"status":"Faliure","Error":f"Got Error {str(e)}"}


@app.get("/getLabour/{labour_id}")
def get_using_labour_id(labour_id):
    labour_services = LabourServices(db.connection)
    result = labour_services.get_labour(labour_id)
    logger.info(f"Type of result {type(result)}")
    return {"status":"Success","data":f"{result}"}

@app.get("/get_all_Labour")
def get_all_labour():
    labour_services = LabourServices(db.connection)
    result = labour_services.get_all_labour()
    return {"status":"Success","data":f"{result}"}







# def login_logout(labour_id=None, first_name=None, last_name=None):
#     attendance_services = AttendanceServices(db.connection)
#     attendance_services.login_logout(labour_id, first_name, last_name)
#     return "Attendance recorded successfully"


# def main():
#     logger.info(create_user("Hari","Sham",500,"labour"))
#     # logger.info(login_logout(first_name="Ram", last_name="Sham"))


# if __name__ == "__main__":
#     main()