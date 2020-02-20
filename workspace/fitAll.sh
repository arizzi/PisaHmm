#!/bin/sh
YEAR=$1
MASS=`seq 1200 5 1300`
for m in $MASS ; do
  
  cd MassScan$m 
  ../fitMass.sh $YEAR $m >& fitmass$YEAR & 
  cd -
done
