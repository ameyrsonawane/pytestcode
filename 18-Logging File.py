import logging
logging.basicConfig(filename="21-log file.txt",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%y-%m-%d %H:%M:%S')
score = 36
if score > 90:
    logging.warning("Log Warning Message")
    print("1st Rank")
elif score > 35:
    logging.warning("Log Critical Message")
    print("Pass")

else:
    logging.warning("Log Error Message")
    print("Fail")