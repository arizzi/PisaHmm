#!/bin/sh
YEAR=$1
MASS=`seq 1250 1 1260`
for m in $MASS ; do
  
  cd MassScan$m 
  ../fitMass.sh $YEAR $m >& fitmass$YEAR & 
  cd -
done
