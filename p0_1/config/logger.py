import functools
import logging
import logging.handlers
import os


LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "app.log")


logger = logging.getLogger(__name__)

def safeRun(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            logger.exception(f"Unhandled error in {func.__name__}")
            print("Something went wrong. Check log files more more  details.")
            return None

    return wrapper
    



def setupLogging():
    os.makedirs(LOG_DIR, exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    fileHandler = logging.handlers.RotatingFileHandler(
        LOG_FILE, maxBytes=5 * 1024, backupCount=3
    )

    fileHandler.setFormatter(formatter)
    fileHandler.setLevel(logging.DEBUG)


    """   consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(formatter)
    consoleHandler.setLevel(logging.WARNING) """

    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.DEBUG)
    rootLogger.addHandler(fileHandler)
    #rootLogger.addHandler(consoleHandler)


    