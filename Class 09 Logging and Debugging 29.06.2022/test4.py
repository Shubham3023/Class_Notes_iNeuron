import logging
logging.basicConfig(filename="test4.log", level= logging.DEBUG , format= '%(levelname)s %(asctime)s %(name)s  %(message)s ')

try:
    logging.info("i am trying to read a file")
    with open("sudh.txt", "r"):
        logging.info("successfully it has read the file")
except Exception as e:
    logging.critical("this is situation for us")
    logging.error(e)
    logging.exception(e)



