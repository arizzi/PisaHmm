#!/bin/sh
#STRING="-o  public_html/syncNoFSRTightPUID/ -f outWithoutJER/"
STRING=" -f out/" # -f outBackup/"

#MASS=`seq 1200 5 1300`
#fewer points to play
MASS=`seq 1200 25 1300`
for m in $MASS ; do
  echo "Launching mass",$m
  mkdir -p workspace/MassScan$m
  DISPLAY="" python plot.py models2017H  -w workspace/MassScan$m --variablesToFit DNN18AtanNoMass___SideBand  DNN18AtanM${m}___SignalRegion  $STRING >& l${m} &
done
   
