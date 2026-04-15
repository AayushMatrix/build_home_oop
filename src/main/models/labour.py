from src.main.models.person import Person,logger

class Labour(Person):
    def __init__(self,first_name,last_name,wage,role):
        super().__init__(first_name,last_name)
        self.wage = wage 
        self.role = role
        # self.crud = crud
        # self.id = self.__save_to_databse(self.crud)   

    def to_dict(self):
        data = super().to_date()
        data.update({"wage":self.wage,"role":self.role})
        return data