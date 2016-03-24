#!/bin/bash

HOST="localhost"
PORT="9090"
KEY="test"
PROCESSES=100

function main() {

    rm -f requests.tmp
    touch requests.tmp
    for I in `seq 1 $1`; do {
        echo "http://$HOST:$PORT/$KEY" >> requests.tmp
    } done;

    cat requests.tmp | xargs -P$PROCESSES -I % wget -qO - % > /dev/null
}

if [ $# -eq 1 ]; then {
    main $1;
    exit $?;
} fi;

echo "Usage: test.sh <number of requests>"
exit 1;

