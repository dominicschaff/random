#!/bin/bash

for ((a=1; a <= 10 ; a++)) ; do
    while [ $(jobs -l | wc -l) -ge 4 ]; do
        sleep 1
        echo "$(date "+%F %T") | Load Average: $(cat /proc/loadavg | cut -f"1 2 3" -d ' ') | Scripts Running: $(jobs -l | wc -l)"
    done
    (python lightning.py "lightning_$a"; echo "completed: $a") &
done

for ((a=1; a <= 10 ; a++)) ; do
    while [ $(jobs -l | wc -l) -ge 4 ]; do
        sleep 1
        echo "$(date "+%F %T") | Load Average: $(cat /proc/loadavg | cut -f"1 2 3" -d ' ') | Scripts Running: $(jobs -l | wc -l)"
    done
    (python lightning_circle_start_center.py "image_$a"; echo "completed: $a") &
done
