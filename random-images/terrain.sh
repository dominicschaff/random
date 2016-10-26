#!/bin/bash


for ((SIZE=11; SIZE <= 13 ; SIZE++)) ; do
    for ((a=1; a <= 10 ; a++)) ; do
        /usr/bin/time -v -o "logs/$SIZE-$a.time" python terrain.py $SIZE "output/$SIZE-$a"
    done
done