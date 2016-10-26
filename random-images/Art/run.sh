#!/bin/bash

gcc -Ofast -lm art.c
(./a.out t0.txt; python art.py t0.txt image0.png) &
(sleep 1;./a.out t1.txt; python art.py t1.txt image1.png) &
(sleep 2;./a.out t2.txt; python art.py t2.txt image2.png) &
(sleep 3;./a.out t3.txt; python art.py t3.txt image3.png) &
