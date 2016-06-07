#!/usr/bin/env python

import re

InFileName = 'Marrus_claudanielis.txt'

InFile = open ( InFileName, 'r')

LineNumber= 0

for Line in InFile:
	Line = Line.strip()

	if LineNumber > 0:
		#print (LineNumber)
		#print (Line)
		Elementlist = Line.split( '\t' )
		#print ( Elementlist )
		print ( 'Depth:{} Lat:{} Lon:{}'.format (Elementlist[4], Elementlist[2], Elementlist[3]))


		SearchString = '(\d+) ([\d\.]+) (\w)'
		Result = re.search( SearchString, Elementlist[2])
		print ( Result.group (1))
		print ( Result.group (2))
		print (	Result.group (3))

		Degree = float (Result.group( 1 ))

		Minute = float (Result.group( 2 ))

		Compass = Result.group( 3 )

		DecimalDegree = Degree + Minute / 60
		if Compass in 'SW':
			DecimalDegree = - DecimalDegree
			
		print DecimalDegree

		#print( Degree ) 

		#print( Minute ) 

		#print( Compass ) 

	LineNumber = LineNumber + 1