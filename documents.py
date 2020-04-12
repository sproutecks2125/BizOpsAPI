#!/usr/bin/python3

__author__ = "Brandon Rickman <brandon.rickman@snhu.edu>"
__version__ = "0.1.0"
__title__ = "Biz System Ops RESTful API"
__license__ = "MIT"


# Main function to run operations and call functions
class Document:
	
	def __init__(self, id, certnum, bizname, date, result, sector, addr):
		self.id = id
		self.certnum = certnum
		self.bizname = bizname
		self.date = date
		self.result = result
		self.sector = sector
		self.addr = addr