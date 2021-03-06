import logging

# setup log stream handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

# setup package logger
logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
logger.addHandler(ch)
