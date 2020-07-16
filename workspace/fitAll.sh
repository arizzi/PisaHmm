#!/bin/sh
YEAR=$1
MASS=`seq 1251 1 1254`
MASS1=`seq 1256 1 1259` 
MASS2=`seq 1200 5 1300`
ALLMASS=$MASS" "$MASS1" "$MASS2
#ALLMASS=`seq 1250 1 1260`
ALLMASS=12538
#ALLMASS="1250 1251 1252 1253 1254 1255 1256 1257 1258 1259 1260"
echo $ALLMASS
for m in $ALLMASS ; do
  
  cd MassScan$m 
  ../fitMass.sh $YEAR $m >& fitmass$YEAR & 
  cd -
done
