# from loguru import logger
# import configparser 

# config = configparser.ConfigParser()

# config.read(r"C:\Users\Aayush-Gyawali\Desktop\python\config_file.ini")

# brick_cost = config["raw_material"]["brick_cost"]

# logger.info(f"{brick_cost}, type of brick_cost {type(brick_cost)}")

# def total_no_of_bricks(length,breadth,height):
#     no_of_brick_in_length_side = length * (height * 2)
#     total_no_of_bricks_in_length_side = no_of_brick_in_length_side*2

#     no_of_brick_in_breadth_side = breadth * (height * 2)
#     total_no_of_bricks_in_breadth_side = no_of_brick_in_breadth_side * 2

#     total_no_of_bricks = total_no_of_bricks_in_length_side + total_no_of_bricks_in_breadth_side

#     return total_no_of_bricks

# def total_cost_for_bricks(config):
#     brick_cost = config["raw_material"]["brick_cost"]
#     total_no_of_brick=total_no_of_bricks(15,15,10)

#     final_cost = float(brick_cost) * total_no_of_brick

#     return final_cost

# result = total_cost_for_bricks(config)

# logger.info(f"Total cost to make 1 room {result}")


from loguru import logger
import configparser 

config = configparser.ConfigParser()

config.read(r"C:\Users\Aayush-Gyawali\Desktop\python\config_file.ini")

brick_cost = config["raw_material"]["brick_cost"]

