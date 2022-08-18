import logging
logging.basicConfig(filename= "mytest3.log", level= logging.DEBUG, format= '%(levelname)s %(asctime)s %(name)s %(message)s')

def divide(a,b) :
    logging.info("we have entered into the function")
    logging.info("the entered vale by user is %s and %s",a,b)
    try:
        div = a/b
        logging.info("we have completed division operation")
        logging.info("the result of division is %s", round(div,2))
    except Exception as e:
        logging.exception(e)
        logging.info("The below log is of error and above log is of exception")
        logging.error(e)
divide(3,0)