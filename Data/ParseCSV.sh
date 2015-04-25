#!/bin/bash

#begin section
awk 'BEGIN {
    FS=","; 
    print "createdUtc@@score@@domain@@title@@author@@up@@down@@totalComments@@permalink@@postUrl" > "QuotesPornParsed.txt" 
		}   
		

		{
			if ($0 ~ /^[0-9].*,$/) { 
				if ($0 ~ /".*,.*"/) printf " ; 
					else printf "%s@@-%s@@-%s@@-%s@@-%s@@-%s@@-%s@@-%s@@-%s@@-%s@@-\n", $1, $2, $3, $5, $6, $7, $8, $9, $10, $21 >> "QuotesPornParsed.txt"
				}		 
		}' QuotesPorn.csv

