#!/bin/bash

for (( i = 0; i < 4; i++ )); do
	python dots.py 500 "dots/dots-$i-" &
done