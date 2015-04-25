#!/usr/bin/env python
import csv
import sys

f = open('QuotesPorn.csv','r')
out = open('QuotesPornParsed.txt','w')
d='%%%'

f_csv = csv.reader(f)

for row in f_csv:
    x=list(row)
    out.write(x[0]+d+x[1]+d+x[4]+d+x[5]+d+x[6]+d+x[7]+d+x[8]+d+x[9]+d+x[20]+'\n')
    
f.close()
out.close()