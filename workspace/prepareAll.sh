#!/bin/sh
YEAR=$1
MASS=`seq 1250 1 1260`
for m in $MASS ; do
  
 cd MassScan$m 
 ../prepareMassDC.sh $YEAR >& lprepare &
 cd -
# cd Mass130Scan$m 
# ../generateToys.sh $YEAR >& lprepare &
# cd -
done
