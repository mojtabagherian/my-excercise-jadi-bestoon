#!/bin/bash

#please set these variables
BASE_URL = http://localhost:8009
mytoken=MZmb1234
curl --data "token=$mytoken&amount=$1&text=$2" $BASE_URL/submit/income/
