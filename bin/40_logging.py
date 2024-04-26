"""
logging library

logging levels
INFO
DEBUG
WARNING
CRITICAL
ERROR
"""

print("logging library")
print("-"*20)
# -----------

import logging

my_logger = logging.getLogger()
my_logger.setLevel(logging.DEBUG)

# prepare log format
my_log_format = logging.Formatter("%(levelname)s : %(filename)s : %(message)s")

# Configure to print on console
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(my_log_format)
my_logger.addHandler(consoleHandler)

# configure to write file as well
fileHandler = logging.FileHandler("my_logging_ex_log.log", "w")
fileHandler.setFormatter(my_log_format)
my_logger.addHandler(fileHandler)

# From now onwards, instead of using print(), make use of below logging function
my_logger.info("This is from info")
my_logger.debug("This is from debug")
my_logger.warning("This is from warning")
my_logger.critical("This is from critical")
my_logger.error("This is from error")

print("#"*40, end="\n\n")
# ###############################

print("Example-1")
print("-"*20)
# -----------

try:
    a = 10
    b = 0
    logging.info(f"Value of 'a' is {a}")
    logging.info(f"Value of 'b' is {b}")
    result = a/b
    logging.info(f"Result is : {result}")
except Exception as e:
    logging.error(f"We got error:{e}")

print("#"*40, end="\n\n")
# ###############################