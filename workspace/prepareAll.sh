#!/bin/sh
YEAR=$1
MASS=`seq 1200 5 1300`
for m in $MASS ; do
  
 cd MassScan$m 
 ../prepareMassDC.sh $YEAR >& lprepare &
 cd -
# cd Mass130Scan$m 
# ../generateToys.sh $YEAR >& lprepare &
# cd -
done
