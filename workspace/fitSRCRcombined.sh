#!/bin/bash
SIGNAL=ch2_DNN18Atan___SignalRegion
SIDE=ch2_DNN18AtanNoMass___SideBand

YEARS="run2016 run2017 run2018"
#YEARS="run2018"
NAME="cmb"
combineCards.py run2016=datacard2016H.txt run2017=datacard2017H.txt run2018=datacard2018H.txt > combined.txt
./decorrelate.sh >> combined.txt

text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel    --channel-masks combined.txt   --PO  'map=.*Hmm.*:r[1.,-10,10]'  >>${NAME}.log

DC=combined.root
combine -M Significance $DC -t -1  --setParameters r=1    >>${NAME}.log
combine -M Significance $DC -t -1  --setParameters r=1  --toysFrequentist  >>${NAME}.log

