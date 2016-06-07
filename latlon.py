#!/usr/bin/env python

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


	LineNumber = LineNumber + 1