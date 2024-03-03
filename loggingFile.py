import logging

logging.basicConfig(filename="test.log", format="%(asctime)s %(levelname)s %(message)s",datefmt="%m/%d/%y %I:%m:%s %p",level=logging.DEBUG)
'''
logging.debug("This is DEBUG")
logging.info("This is Info")
logging.error("This is Error")
logging.warning("This is Warning")
logging.critical("This Is critical")
'''
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logging.debug("This is DEBUG")
logging.info("This is Info")
logging.error("This is Error")
logging.warning("This is Warning")
logging.critical("This Is critical")