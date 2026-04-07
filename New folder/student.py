from  loguru import logger

import configparser
student_details = {1:["math","history"],2:["biology","chemistry","history"],3:["science"]}

config = configparser.ConfigParser()
config.read(r'C:\Users\Aayush-Gyawali\Desktop\python\book.ini')

book_price = {book.lower():int(price)
              for book,price in config[' '].items()}

logger.info(f"Book price: {book_price}")

filtred = { key: value # expression 
            for key,value in student_details.items() # loop 
            if len(value)>= 2 }  # filter 


for student_id ,subjects in filtred.items():
    total_cost = 0
    for subject in subjects:
        price = book_price.get(subject.lower(),0)

        total_cost += price

    discount = total_cost * 0.10
    final_cost = total_cost-discount

    logger.info(f"{final_cost}")



# logger.info(filtred)


