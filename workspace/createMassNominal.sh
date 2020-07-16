#!/bin/bash
FIRST=6
YEAR=$1
MASS=`seq 1251 1 1254`
MASS1=`seq 1256 1 1259`
MASS2=`seq 1200 5 1300`
ALLMASS=$MASS" "$MASS1" "$MASS2
#ALLMASS="1200 1205 1210 1215 1220 1225 1230 1235 1240 1245 1265 1270 1275 1280 1285 1290 1295 1300"
#LLMASS="1265 1270 1275 1280 1285 1290 1295 1300"
#ALLMASS=`seq 1250 1 1260`
ALLMASS="12538"
echo $ALLMASS
for m in $ALLMASS ; do
  cd MassScan$m
#  combineCards.py DNN18AtanNoMass___SideBand=datacard${YEAR}HSB.txt DNN18AtanM${m}___SignalRegion=datacard${YEAR}HSR.txt > datacard${YEAR}H.txt

  ../makerateparam1.sh ${YEAR} H
  cd -
  F=MassScan$m/datacard${YEAR}H.txt
  FO=MassScan$m/datacard${YEAR}Hnominal.txt
  N=`wc -l $F | awk '{print $1}'`
  LAST=$[$N-$FIRST]
  echo $N $FIRST $LAST
STRING='''
shapes ggHmm_YYYYAMCPY DNN18AtanMXXXX___SignalRegion  ../MassScan1250/fileCombineYYYYH.root DNN18AtanM1250_DNN18AtanM1250___SignalRegion_$PROCESS DNN18AtanM1250_DNN18AtanM1250___SignalRegion_$PROCESS_$SYSTEMATIC\nshapes vbfHmm_YYYYAMCPY DNN18AtanMXXXX___SignalRegion  ../MassScan1250/fileCombineYYYYH.root DNN18AtanM1250_DNN18AtanM1250___SignalRegion_$PROCESS DNN18AtanM1250_DNN18AtanM1250___SignalRegion_$PROCESS_$SYSTEMATIC
'''
UPDATE=`echo $STRING | perl -pe 's/XXXX/'$m'/g; s/YYYY/'$YEAR'/g'`
head -n $FIRST $F > $FO
echo -e $UPDATE >> $FO
tail -n $LAST $F >> $FO

done
