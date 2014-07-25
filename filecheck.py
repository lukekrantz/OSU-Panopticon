#!/usr/bin/env python
import sys, os, re


file = open("webbugs.graphml")
first = set() #built-in set type
for line in file:
	for letter in line:
		first.add(letter)
			
file = open("cookies.graphml")

second = set()
for line in file:
	for letter in line:
		second.add(letter)
		
					
print second - first
