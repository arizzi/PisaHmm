#!/bin/bash
SIGNAL=DNN18Atan___SignalRegion
SIDE=DNN18AtanNoMass___SideBand

YEAR=$1
text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel    --channel-masks datacard${YEAR}H.txt   --PO  'map=.*Hmm.*:r[1.,-10,10]'  >${YEAR}.log
text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel    --channel-masks datacard${YEAR}Hnominal.txt   --PO  'map=.*Hmm.*:r[1.,-10,10]'  >${YEAR}.log

DC=datacard${YEAR}H.root
DCnominal=datacard${YEAR}Hnominal.root

echo combine -M Significance  -t -1 $DC --setParameters mask_${SIGNAL}=0,mask_${SIDE}=0,r=1   --toysFrequentist
combine -M Significance  -t -1 $DC --setParameters mask_${SIGNAL}=0,mask_${SIDE}=0,r=1   --toysFrequentist  >>${YEAR}.log
echo combine -M MultiDimFit -n$YEAR  -t -1 $DC --setParameters mask_${SIGNAL}=0,mask_${SIDE}=0,r=1   --toysFrequentist  --saveToys

combine -M MultiDimFit -n$YEAR -t -1 $DC --setParameters mask_${SIGNAL}=0,mask_${SIDE}=0,r=1   --toysFrequentist  --saveToys >>${YEAR}.log

combine -M MultiDimFit -n$YEAR -t -1 $DCnominal --setParameters r=1  --toysFrequentist  --toysFile higgsCombine${YEAR}.MultiDimFit.mH120.123456.root 


