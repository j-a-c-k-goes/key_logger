#!/usr/bin/python3.11
import logging, sys, os
class LogFile:
	def __init__( self ):
		pass
	def determine_log_type( self ):
		''' based on operating system, returns appropriate log file path '''
		if ( sys.platform == 'win32' ) or ( sys.platform == 'cygwin' ):
			''' windows system '''
			log_file = os.environ['TEMP'] + '\\keys.log'
		else:
			''' linux, macos, other '''
			log_file = '/tmp/keys.log'
		return log_file
	def config(self, log_file):
		''' 
			configuration for log file 

			parameters:
				filename(str): this is the log file and its absolute path
				level(int): represents levels of logging (https://docs.python.org/3/library/logging.html)
				format(str): content format is timestamp then content
		'''		
		# logging configuration includes a log file, level, and format
		config = logging.basicConfig( filename=log_file, level=logging.INFO, format='%(asctime)s: %(message)s'  )
		return config
