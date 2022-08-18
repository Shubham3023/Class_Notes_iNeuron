import logging
logging.basicConfig(filename= "test3.log", level= logging.INFO , format= '%(levelname)s %(asctime)s %(name)s  %(message)s ')

def divide(a,b) :
    logging.info("The number entered by user is %s and %s",a,b)
    try:
        logging.info("we are into function")
        div = a/b
        logging.info("we have completed a division operation")
        logging.info("result of code is %s", round(div,2))
    except Exception as e:
        logging.exception(e)

divide(3,7)
