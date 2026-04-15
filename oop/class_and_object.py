from loguru import logger

class Person:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name 
        self.email = self.first_name + "." + self.last_name + "@gmail.com"

    def print_detail(self):
        return f"Your first name is set as {self.first_name} and last name is {self.last_name} with email id as {self.email}"

class Labour1(Person):
    def __init__(self, first_name, last_name,wage):
        super().__init__(first_name, last_name,)
        self.wage = wage      

    def print_detail(self):
        return f"Your first name is set as {self.first_name} and last name is {self.last_name} with email id as {self.email} and total wage is {self.wage}"
    pass


class Mistri(Labour1):
    def __init__(self, first_name, last_name,wage,skill):
        super().__init__(first_name, last_name,wage)
        self.skill = skill  

    
    def print_detail(self):
        return f"Your first name is set as {self.first_name} and last name is {self.last_name} with email id as {self.email} and total wage is {self.wage} skill {self.skill} "
class Labour(Person):
    no_of_labours = 0
    def __init__(self,first_name,last_name,wage):
        self.first = first_name
        self.last = last_name
        self.wage = wage
        Labour.no_of_labours += 1  
       

    def save_to_databse(self,db_connection):
        query = "select id from labours where lower(first_name) = %s AND lower(last_name) = %s"
        result = self.crud.read_from_pos(query,(self.first_name,self.last_name))

        if result:
            logger.info(f"Labour already exixts with ID: {result[0][0]}")
            return result[0][0]
        # db_connection.save()

    def login(self):
        pass 

    @classmethod
    def total_no_of_labours(cls):
        return Labour.no_of_labours

    @staticmethod
    def is_valid_wage(your_wage):
        if your_wage<200:
            logger.info("Ask for a wages")
        else:
            logger.info("Your wahe is more")
        

# print(Labour.no_of_labours)
# print(Labour.is_valid_wage(400))
# mansih = Labour("manish","kumar",500)
# print(Labour.no_of_labours)
# ram = Labour("Ram","Sing",400)
# print(Labour.no_of_labours)
# print(ram.total_count)

# person1 = Person("manish","kumar")
# logger.info(person1.print_detail())
# logger.info(person1.email)

obj = Mistri("manish","Kumar",1000,"Plumbing")
print(help(obj))
# logger.info(obj.print_detail())