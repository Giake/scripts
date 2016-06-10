#!/usr/bin/env python

import re
import sys

def decimalat (DegreeString):
	#Converts a string for latitude or longitude into a float
	SearchString = '(\d+) ([\d\.]+) (\w)'
	Result = re.search( SearchString, DegreeString)
	print ( Result.group (1))
	print ( Result.group (2))
	print (	Result.group (3))

	Degree = float (Result.group( 1 ))
	Minute = float (Result.group( 2 ))
	Compass = Result.group( 3 )
	DecimalDegree = Degree + Minute / 60

	if Compass in 'SW':
		DecimalDegree = - DecimalDegree

	return DecimalDegree

assert( decimalat('36 30.0 N') == 36.5)
assert( decimalat('36 30.0 S') == -36.5)
assert( decimalat('36 30.0 W') == -36.5)

arguments = sys.argv
print (arguments)

InFileName = sys.argv[1]

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

		latitude = decimalat ( Elementlist [2])
		print (latitude)



		

		#print( Degree ) 

		#print( Minute ) 

		#print( Compass ) 

	LineNumber = LineNumber + 1