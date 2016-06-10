#!/usr/bin/env python

#the original DNASeq is immediately written over when I give it another meaning
DNASeq = "ATGAACAATTCCCGGGGATCAGCTTCGCGAGCAGTTTACGT"
#DNASeq = raw_input(" Enter a DNA sequence: ")
DNASeq = DNASeq.upper()
DNASeq = DNASeq.replace(" ","")



print ('Sequence ' + DNASeq)

SeqLength = float ( len( DNASeq ))


print ('Length is ' + str ( SeqLength))


#NumberA = DNASeq.count('A')
#NumberT = DNASeq.count('T')
#NumberG = DNASeq.count('G')
#NumberC = DNASeq.count('C')


#print ("A: {}".format (NumberA / SeqLength))
#print ("T: {}".format (NumberA / SeqLength))
#print ("G: {}".format (NumberA / SeqLength))
#print ("C: {}".format (NumberA / SeqLength))

#instead of putting all these commands above we make a loop


#BaseDict= { 'A': 0, 'T': 0, 'G':0, 'C':0}

Bases = 'CGTA'

TotalStrong = 0
TotalWeak = 0

for Base in Bases:

	Count = DNASeq.count ( Base )
	Frequency = DNASeq.count ( Base ) / SeqLength

	print ( '{}: {:.2f}'.format(Base, Frequency))
	if Base in 'GC':
		TotalStrong = TotalStrong + Count
	elif Base in 'TA':
		TotalWeak = TotalWeak + Count

print ( TotalStrong, TotalWeak)

#This does the same thats why i made it text

#TotalStrong = 0
#TotalWeak = 0

#for Base in DNASeq:
#	if Base in "GC":
#		TotalStrong = TotalStrong + 1
#	else:
#		TotalWeak = TotalWeak + 1
#print (TotalStrong,TotalWeak)

Counts= dict()
for Base in Bases:
	Count = DNASeq.count (Base)

print "Done"



if SeqLength <= 14:

	MeltTemp = ( 4 * TotalStrong ) + ( 2 * TotalWeak )

	#print ( 'Melting Temp: {}').format(MeltTemp)

else:
	MeltTemp = 64.9 + 41 * (TotalStrong - 16.4 / SeqLength)

	#print ( 'Long melting Temp: {}'.format(MeltTemp))

print ( 'Melting Temp: {}'.format(MeltTemp))

print ('Done')

#if is a way to say which lines of codes are executed depending on other parameters)
