import logging
import Utitlities.logCreator as lc
def log_generator():
    logging.basicConfig(
        filename="testlogreport.log",
        level=logging.INFO
        format='%(asctime)s -%(levelnamme)s -%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %p'
    )
    return logging.getLogger()
