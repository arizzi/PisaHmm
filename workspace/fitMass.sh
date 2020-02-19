#!/bin/bash
SIGNAL=DNN18Atan___SignalRegion
SIDE=DNN18AtanNoMass___SideBand

YEAR=$1
#text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel    --channel-masks datacard${YEAR}H.txt   --PO  'map=.*Hmm.*:r[1.,-10,10]'  >${YEAR}.log
#text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel    --channel-masks datacard${YEAR}Hnominal.txt   --PO  'map=.*Hmm.*:r[1.,-10,10]'  >${YEAR}.log

DC=datacard${YEAR}H.root
DCnominal=datacard${YEAR}Hnominal.root


combine -M MultiDimFit -t -1 $DCnominal --setParameters r=1  --toysFrequentist  --toysFile higgsCombineTest.MultiDimFit.mH120.123456.root  > r.txt
combine -M Significance -t -1 $DCnominal --setParameters r=1  --toysFrequentist  --toysFile higgsCombineTest.MultiDimFit.mH120.123456.root  > sig.txt
combine -M Significance -t -1 $DCnominal --setParameters r=1  --toysFrequentist  --toysFile higgsCombineTest.MultiDimFit.mH120.123456.root --pvalue  > pval.txt



