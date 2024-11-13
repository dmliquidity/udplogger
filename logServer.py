import random
import time
from udp_server import UDPServer
import logging

logger = logging.getLogger('updServer')

class LogServer(object):

    def __init__(self, name):
        self.name = name
        self.log_server = UDPServer(host='', port=9090)

    def boot(self):
        logger.debug("Booting Log Server")
        self.log_server.start()

