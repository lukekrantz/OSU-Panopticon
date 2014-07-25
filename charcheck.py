#!/usr/bin/env python
#test comment

import sys, os, re
from pysqlite2 import dbapi2 as sqlite


domain_re = re.compile('.*\/\/(?P<domain>.*?)\/')
sqlitedbname = "2days.db"
connection = sqlite.connect(sqlitedbname)
connection.row_factory = sqlite.Row
cursor = connection.cursor()

query = 'select host,referer from rawpkt where status="200" and contenttype like "image/gif%" and contentlength < 35'
cursor.execute(query)

first = set() #built-in set type
for row in cursor:
	for letter in row['host']:
		first.add(letter)
	domain_result = domain_re.match(str(row['referer']))
	if (domain_result):
		domain = domain_result.group('domain')
		for letter in domain:
			first.add(letter)
			
query = 'select host,referer from rawpkt where status="200" and contenttype like "image/gif%" and contentlength = 35'
cursor.execute(query)
second = set()
for row in cursor:
	for letter in row['host']:
		second.add(letter)
	domain_result = domain_re.match(str(row['referer']))
	if (domain_result):
		domain = domain_result.group('domain')
		for letter in domain:
			second.add(letter)
			
print second - first
