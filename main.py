import time
from logServer import LogServer
import logging
import argparse
import os
import sys

parser = argparse.ArgumentParser(description='Log Server')

loglevel_default = os.environ.get('LOG_LEVEL') or 'DEBUG'
parser.add_argument('-l', '--loglevel', type=str, required=False,
					default=loglevel_default, help='Specify the conversion type')
args = parser.parse_args()

logger = logging.getLogger('updServer')

def configure_default_handler():
    # Create a default handler for stdout
    log_level = getattr(logging, args.loglevel.upper())
    format = '%(asctime)s - %(module)s - %(levelname)s - %(message)s'

    logging.basicConfig(level=logging.DEBUG, format=format)
    # handler = logging.StreamHandler(sys.stdout)
    # formatter = logging.Formatter(format)
    # handler.setFormatter(formatter)
    # # Set the default logging level
    # handler.setLevel(log_level)

    # Configure all existing loggers to use the default handler
    # for logger_name in logging.root.manager.loggerDict.keys():
    #     logger = logging.getLogger(logger_name)
    #     logger.addHandler(handler)

# Configure the default handler for all loggers
configure_default_handler()

logger.info('booting...')
ls = LogServer("HAL")
ls.boot()

while True:
    logger.info('waiting...')
    time.sleep(5)
    pass
 
logger.info('Exiting...')