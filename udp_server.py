import socket
import threading
import time
import struct
import logging
import select

# Create a logger for the UDPServer
logger = logging.getLogger('UDPServer')

logger.setLevel(logging.DEBUG)  # Set the logging level of this logger

# logger.propagate = False

# Create a file handler that logs even debug messages
# fh = logging.FileHandler('udp_server.log')
# fh.setLevel(logging.DEBUG)

# # Create a formatter and set it for the handler
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# fh.setFormatter(formatter)

# # Add the handler to the logger
# logger.addHandler(fh)

# If you want to log to both file and console, uncomment the following lines
# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# console.setFormatter(formatter)
# logging.getLogger('').addHandler(console)


class UDPServer:
    def __init__(self, host='', port=9090):
        self.host = host
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_t = threading.Thread(target=self.server_thread)
        self.server_t.daemon = True
        self.running = False
    
    def server_thread(self):       
        self.running = True
        self.s.bind((self.host, self.port))
        try:
            while self.running:
                try:
                    data, address = self.s.recvfrom(1024)
                    message = data.decode('utf-8')
                    logger.info(f"{address} -> {message}")
                except Exception as e:
                    logger.error(f'Error UDP: {e}')
        except KeyboardInterrupt:
            logger.warn('Server terminated by user')
        except Exception as e:
            logger.error(f'Error occurred while running server: {e}')
        finally:
            self.s.close()
    
    def start(self):
        logger.info(f'Starting UPD server on {self.host}:{self.port}')
        self.server_t.start()
    
    def stop(self):
        self.running = False
        self.s.close()
        self.server_t.join()

