#!/bin/bash

source venv/bin/activate &
python students/app/api.py &

COUNTDOWN=30

postname(){
COUNT="0"
index=$RANDOM
let "index %= 30"

echo $COUNT
echo $index

# while (("$COUNT" < "$index"))
# do
# 	while read line
# 	do
# 		NAMEVAR=$line
# 	done
# 	COUNT=$COUNT+1
# done < $1

NAMEVAR=$(less 50names.txt | awk '{print $($index);}' )

echo $NAMEVAR
curl -X POST -H "Content-Type: application/json" -d '{"name":"$NAMEVAR"}' http://localhost:5000/students/
}

while (("$COUNTDOWN" > "0"))
do
	postname
	COUNTDOWN=$COUNTDOWN+1
done