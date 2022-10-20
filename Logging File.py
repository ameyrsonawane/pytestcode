import logging
logging.basicConfig(filename="log file.txt",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
score = 34.9
if score > 90:
    logging.warning("Log Warning Message")
    print("1st Rank")
elif score > 35:
    logging.warning("Log Critical Message")
    print("Pass")

else:
    logging.warning("Log Error Message")
    print("Fail")