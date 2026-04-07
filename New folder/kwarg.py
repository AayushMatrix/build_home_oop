from loguru import logger

"""

def final_cart_amount(*args, discount):
    total_amount = 0
    for amount in args:
        total_amount += amount
    amount_after_discount = total_amount - (total_amount * discount)
    return amount_after_discount


final_amount = final_cart_amount(100, 500,100,300,500,discount = 0.5)

logger.info(final_amount)

"""

def write_logs(**kwargs):
    """
    Write logs to a file using **kwargs
    
    Args:
        **kwargs: Keyword arguments containing log entries
        filename: Optional filename (default: 'logs.txt')
        mode: File mode 'w' or 'a' (default: 'w')
    """
    # Extract special parameters
    filename = kwargs.pop('filename', 'logs.txt')
    mode = kwargs.pop('mode', 'a')
    
    # Write logs to file
    with open(filename, mode) as file:
        for key, value in kwargs.items():
            file.write(f"{key}: {value}\n")
    
    print(f"{len(kwargs)} log entries saved to '{filename}'")

# Example usage
write_logs(
    log1="User logged in",
    log2="File uploaded",
    log3="Settings updated",
    filename="system_logs.txt"
)

def write_log(**logges):
    filename = logges.pop('filename')
    
