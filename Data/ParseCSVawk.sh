#!/bin/bash

awk 'BEGIN { FS = ","; print "{\n" } ; {print "\t{\"created_utc\": \"" $1 "\", \"score\": \"" $2 "\", \"title\": \" $5 "\", \"author\": \" $6 "\", \"ups\": \" $7 "\", \"downs\": \" $8 "\", \"num_comments\": \" $9 "\", \"permalink\": \" $10 "\", \"url\": \" $21 "\"}\n"} END {print "}"} ' QuotesPorn.csv > QuotesPornParsed.json