#!/bin/bash
SIGNAL=DNN18Atan___SignalRegion
SIDE=DNN18AtanNoMass___SideBand

YEAR=$1
#text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel    --channel-masks datacard${YEAR}H.txt   --PO  'map=.*Hmm.*:r[1.,-10,10]'  >${YEAR}.log
#text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel    --channel-masks datacard${YEAR}Hnominal.txt   --PO  'map=.*Hmm.*:r[1.,-10,10]'  >${YEAR}.log

DC=datacard${YEAR}H.root
DCnominal=datacard${YEAR}Hnominal.root


#ombine -M MultiDimFit -t -1 $DCnominal --setParameters r=1  --toysFrequentist  --toysFile higgsCombineTest.MultiDimFit.mH120.123456.root  --verbose 9 > r${YEAR}.txt
#ombine -M Significance -t -1 $DCnominal --setParameters r=1  --toysFrequentist  --toysFile higgsCombineTest.MultiDimFit.mH120.123456.root --verbose 9 > sig${YEAR}.txt
#ombine -M Significance -t -1 $DCnominal --setParameters r=1  --toysFrequentist  --toysFile higgsCombineTest.MultiDimFit.mH120.123456.root --pvalue --robustHesse 1  --verbose 9 > pval${YEAR}.txt
combine -M Significance --pvalue  -t -1 $DCnominal --setParameters r=1  --toysFrequentist  --toysFile higgsCombineTest.MultiDimFit.mH120.123456.root   --verbose 9 > pval${YEAR}.txt


#combine -M MultiDimFit -t -1 $DCnominal --robustFit 1 --setParameters r=1  --toysFrequentist  --toysFile ../Mass130Scan$2/higgsCombineTest.MultiDimFit.mH120.123456.root  > r${YEAR}130.txt
#combine -M Significance -t -1 $DCnominal --setParameters r=1  --toysFrequentist  --toysFile ../Mass130Scan$2/higgsCombineTest.MultiDimFit.mH120.123456.root  > sig${YEAR}130.txt
#combine -M Significance -t -1 $DCnominal --setParameters r=1  --toysFrequentist  --toysFile ../Mass130Scan$2/higgsCombineTest.MultiDimFit.mH120.123456.root --pvalue  > pval${YEAR}130.txt


