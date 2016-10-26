#!/bin/bash

if [ $# -eq 1 ]; then
	echo "Using file: $1"
else
	echo "Need file"
	exit 1
fi

header=$(head -n1 "$1")
tail -n +2 "$1" > tempstart
split -l50000 tempstart tempsplit
for i in tempsplit*; do
	echo "$header" | cat - "$i" > tempfile
	mv tempfile "$i.csv"
	rm "$i"
done
rm tempstart
