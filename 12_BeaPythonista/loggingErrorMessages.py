import logging
logging.basicConfig(level='DEBUG', filename='blue_ox.log')
logger = logging.getLogger('bunyan')
logger.debug("Where's my axe?")
logger.warning("I need my axe")

logging.debug("Looks like rain")
logging.info("And hail")
logging.warning("Did I hear thunder?")
logging.error("Was that lightning?")
logging.critical("Stop fencing and get inside!")
