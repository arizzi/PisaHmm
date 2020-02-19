#!/bin/bash
FIRST=6
YEAR=$1
MASS=`seq 1200 5 1300`
for m in $MASS ; do
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
