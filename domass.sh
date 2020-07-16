#!/bin/sh
#STRING="-o  public_html/syncNoFSRTightPUID/ -f outWithoutJER/"
STRING=" -f out/" #LowMass/" # -f outBackup/"
YEAR=$1
#MASS=`seq 1200 5 1300`
#fewer points to play
#MASS=`seq 1200 5 1300`
#MASS=`seq 1200 5 1245`
#MASS=`seq 1250 1 1260`
#MASS=`seq 1260 5 1300`
MASS="12538"
for m in $MASS ; do
  echo "Launching mass",$m
  mkdir -p workspace/MassScan$m
  DISPLAY="" python plot.py models${YEAR}H  -w workspace/MassScan$m --variablesToFit DNN18AtanNoMass___SideBand  DNN18AtanM${m}___SignalRegion  $STRING >& l${m}-${YEAR} &
done
   
