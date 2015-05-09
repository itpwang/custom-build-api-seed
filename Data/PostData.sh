#!/bin/bash

sed -i -e 's/"/ /g' QuotesPornParsed.txt
sed -i -e "s/'/ /g" QuotesPornParsed.txt

awk 'BEGIN {FS = "%%%"; printf "#!/bin/bash\n" > "postqueries.sh"} {
    printf "curl -X POST -H \"Content-Type:application/json\" -d \x27{ \"createdUtc\":%-s, \"score\":%-s, \"title\":\"%-s\", \"author\":\"%-s\", \"ups\":%-s, \"downs\":%-s, \"num_comments\":%-s, \"permalink\":\"%-s\", \"url\":\"%-s\" }\x27 http://localhost:5000/QuotesPorn/\n ", $1, $2, $3, $4, $5, $6, $7, $8, $9 > "postqueries.sh"
}' QuotesPornParsed.txt

sed '2d' postqueries.sh > postqueries.sh