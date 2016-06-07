#!/usr/bin/env python

InFileName = 'Marrus_claudanielis.txt'

InFile = open ( InFileName, 'r')

for Line in InFile:
	Line = Line.strip()
	print (Line)