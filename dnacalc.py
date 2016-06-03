#!/usr/bin/env python

#the original DNASeq is immediately written over when I give it another meaning
DNASeq = "ATGAAC"
DNASeq = raw_input(" Enter a DNA sequence: ")
DNASeq = DNASeq.upper()
DNASeq = DNASeq.replace(" ","")



print ('Sequence ' + DNASeq)

SeqLength = float ( len( DNASeq ))


print ('Length is ' + str ( SeqLength))

NumberA = DNASeq.count('A')
NumberT = DNASeq.count('T')
NumberG = DNASeq.count('G')
NumberC = DNASeq.count('C')

print('A: ' + str ( NumberA / SeqLength ))
print('T: ' + str ( NumberT / SeqLength ))
print('G: ' + str ( NumberG / SeqLength ))
print('C: ' + str ( NumberC / SeqLength ))

