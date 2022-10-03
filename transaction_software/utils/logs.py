"""
Generate logs incase of any errors, warnings, informations, etc.,
"""

import logging
import os
from os.path import exists, join


log_file_path = "transaction_software\\logs\\"

# Check for the existence of logs directory if not create one.
if exists(log_file_path) is not True:
    DIR = "logs\\"
    parent_dir = os.getcwd()+"\\transaction_software\\"
    path = join(parent_dir, DIR)
    os.mkdir(path)


def database_error(msg:str,line_no:int)->None:
    """
    Write a log on database error to the database.log
    """

    Format = "[%(asctime)s] %(levelname)s: [line: {line}] {module}.py - {message}".format(message=msg, module="database",line= line_no)

    # setting the logger name
    logger = logging.getLogger('database')

    # adding the file handler
    f_handler = logging.FileHandler(log_file_path+'database.log', mode='w')

    f_handler.setLevel(logging.ERROR)
    # adding the format of the log
    f_formatter = logging.Formatter(fmt=Format)

    f_handler.setFormatter(f_formatter)
    logger.addHandler(f_handler)
    logger.error(msg=msg,exc_info=True)

# drive code
if __name__=='__main__':
    pass
