#!/bin/bash

source venv/bin/activate &
python students/app/api.py &

curl --request GET http://localhost:5000/students/

curl -X POST -H "Content-Type: application/json" -d '{"name":"Ivan"}' http://localhost:5000/students/

curl -X GET http://localhost:5000/students/2

curl -X PUT -H "Content-Type: application/json" -d '{"name":"Change"}' http://localhost:5000/students/3

curl http://localhost:5000/students/3