#!/usr/bin/env python

#the original DNASeq is immediately written over when I give it another meaning
DNASeq = "ATGAAC"
#DNASeq = raw_input(" Enter a DNA sequence: ")
DNASeq = DNASeq.upper()
DNASeq = DNASeq.replace(" ","")



print ('Sequence ' + DNASeq)

SeqLength = float ( len( DNASeq ))


print ('Length is ' + str ( SeqLength))

NumberA = DNASeq.count('A')
NumberT = DNASeq.count('T')
NumberG = DNASeq.count('G')
NumberC = DNASeq.count('C')


print ("A: {}".format (NumberA / SeqLength))
print ("T: {}".format (NumberA / SeqLength))
print ("G: {}".format (NumberA / SeqLength))
print ("C: {}".format (NumberA / SeqLength))

TotalStrong = NumberG + NumberC
TotalWeak = NumberA + NumberT

if SeqLength <= 14:

	MeltTemp = ( 4 * TotalStrong ) + ( 2 * TotalWeak )

	#print ( 'Melting Temp: {}').format(MeltTemp)

else:
	MeltTemp = 64.9 + 41 * (TotalStrong - 16.4 / SeqLength)

	#print ( 'Long melting Temp: {}'.format(MeltTemp))

print ( 'Melting Temp: {}'.format(MeltTemp))

print ('Done')

#if is a way to say which lines of codes are executed depending on other parameters)
