#!/bin/bash

control_c()
{
  echo -en "\n*** Ouch! Exiting ***\n"; rm a.out; exit $?
}
trap control_c SIGINT

echo "main(t){for(t=0;;t++)putchar($(case $1 in
    1 ) echo "(t*(\"36364689\"[t>>13&7]&15))/12&128)+(((((t>>12)^(t>>12)-2)%11*t)/4|t>>13)&127";;
    * ) echo "t*(((t>>12)|(t>>8))&(63&(t>>4)))";;
esac));}" | gcc -xc -

./a.out
