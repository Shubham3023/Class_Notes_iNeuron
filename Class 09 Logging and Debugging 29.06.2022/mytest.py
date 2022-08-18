import logging
logging.basicConfig(filename="mytest.log", level= logging.DEBUG, )
l = [1,2,3,4,5]
for i in l :
    logging.info("we have entered in for loop")
    logging.info(i)
logging.warning("for loop has executed")

"""
Logging has 5 levels
1) DEBUG (10) 2) INFO (20) 3) WARNING (30) 4) ERROR (40) 5) CRITICAL (50)

If DEBUG is used as level, then all logs will be displayed.

If INFO is used as level, then all logs will be displayed except debug logs.  

If WARNING is used as level, then all logs will be displayed except debug, info logs.

If ERROR is used as level, then all logs will be displayed except debug, info, warning logs.

If CRITICAL is used as level, then only critical logs will be displayed .
"""