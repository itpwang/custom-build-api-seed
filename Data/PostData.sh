#!/bin/bash

awk 'BEGIN {FS = "%%%"; printf "#!/bin/bash\n" > ""} {
    printf "curl -X POST -H \"Content-Type:application/json\" -d \x27{ \"party\":\"%-s\", \"createdUtc\":%-s, \"score\":%-s, \"domain\":\"%-s\", \"title\":\"%-s\", \"author\":\"%-s\", \"ups\":%-s, \"downs\":%-s, \"numComments\":%-s, \"permaLinks\":\"%-s\", \"thumbNail\":\"%-s\", \"urlImg\":\"%-s\" }\x27 http://localhost:5000/politics/\n ", $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12 > "dataQueries.sh"
}' QuotesPornParsed.txt