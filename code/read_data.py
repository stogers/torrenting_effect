#!/usr/bin/python2.7
# -*- coding: utf8 -*-

import csv
import pandas as pd
import xml.etree.ElementTree as ET

class Data:


	def __init__(self):
		pass

	def read_from_xml(self, filename):
		f = open(filename, 'rb')
		tree = ET.parse(filename)
		print root

	def read_from_csv(self, filename):
		csvfile = open(filename, 'rb')
		data = csv.reader(csvfile, delimiter="\t")
		first_line = True
		self.header = data.next()
		self.data = pd.DataFrame.from_csv(filename, sep='\t')

d = Data()
d.read_from_csv("../data/rottentomato/movies.dat")
# print d.data.shape

d2 = Data()
d2.read_from_xml("../data/piratebay_wrapped.xml")

# print d2.data.shape