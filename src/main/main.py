from src.main.databases.postgre_connector import logger,PostgresConnection,PostgresCRUDOperation
# from src.main.labours.labour_class import Labour,Person, Mistri
from src.main.factories.person_factory import PersonFactory
from src.main.services.attendance_service import AttendanceServices
from src.main.services.labour_service import LabourServices
from fastapi import FastAPI,HTTPException
from src.main.models.all_models import User, UIResponse,Attendance


import configparser
config = configparser.ConfigParser()
config.read(r"C:\Users\Aayush-Gyawali\Desktop\python\src\resources\config_file.ini")


db = PostgresConnection.get_instance(config)

app = FastAPI(title="API to build Home", description="Building roboust design")


# @app.post("/postcreateUser")
# def create_user(first_name, last_name, wage, role):
#     try:
#         labour = PersonFactory.create_person(
#             role,
#             first_name=first_name,
#             last_name=last_name,
#             wage=wage,
#             role=role
#         )
#         labour_service = LabourServices(db.connection)
#         labour_id = labour_service.create_labour(labour)
#         return {"status":"Sucess","message":f"User created with ID {labour_id}"}
    
#     except Exception as e:
#         return {"status":"Faliure","Error":f"Got Error {str(e)}"}

@app.post("/postcreateUser",tags=["User"])
def create_user(user:User):
    try:
        user = user.model_dump()
        # logger.info(f"Value of User is {user}")
        labour = PersonFactory.create_person(
            user['role'],
            first_name=user['first_name'],
            last_name=user['last_name'],
            wage=user['wage'],
            role=user['role']
        )
        labour_service = LabourServices(db.connection)
        labour_id = labour_service.create_labour(labour)
        return UIResponse(status="Success",status_code=200,data = user,message=f"User created with Id {labour_id}")
        # return {"status":"Sucess","message":f"User created with ID {labour_id}"}
     
    except Exception as e:
        # raise HTTPException(status_code=400,detail=f"Got Error {str(e)}")
        return UIResponse(status="Fail",status_code=400,data = user,message=f" got Error {str(e)}")

        # return {"status":"Faliure","Error":f"Got Error {str(e)}"}



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


@app.post("/postattendance")
def login_logout(attendance:Attendance):
    attendance = attendance.model_dump()
    attendance_services = AttendanceServices(db.connection)
    attendance_services.login_logout(attendance["labour_id"], attendance["first_name"], attendance["last_name"])
    return UIResponse(status="Sucess",status_code=200,data = None,message=f"Attendance recorded sucessfully")
    # return "Attendance recorded successfully"


# def main():
#     logger.info(create_user("Hari","Sham",500,"labour"))
#     # logger.info(login_logout(first_name="Ram", last_name="Sham"))


# if __name__ == "__main__":
#     main()