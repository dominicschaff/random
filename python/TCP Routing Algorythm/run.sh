#!/bin/bash

if [ $1 -eq -1 ]; then
    for i in $(seq 0 1 11)
    do
        echo -n "Enter to start: $i"
        read ar
        python client.py $i
    done
elif [ $1 -eq -2 ]; then
    echo "RUNNING SERVER"
    for i in $(seq 0 1 11)
    do
        python server.py
    done
    for i in $(seq 0 1 11)
    do
        for j in $(seq 0 1 11)
        do
            python graph_plot.py $i $j
        done
    done

else
    for i in $(seq 0 1 11)
    do
        echo -n "Enter to start: $i"
        read ar
        python client.py $i
    done
fi
