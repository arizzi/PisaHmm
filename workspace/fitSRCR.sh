#!/bin/bash
SIGNAL=DNN18Atan___SignalRegion
SIDE=DNN18AtanSpread___SideBand

YEAR=$1
text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel    --channel-masks datacard${YEAR}H.txt   --PO  'map=.*Hmm.*:r[1.,-10,10]'  >${YEAR}.log

DC=datacard${YEAR}H.root

combine -M Significance  -t -1 $DC --setParameters mask_${SIGNAL}=0,mask_${SIDE}=0,r=1    >>${YEAR}.log
combine -M Significance  -t -1 $DC --setParameters mask_${SIGNAL}=0,mask_${SIDE}=0,r=1   --toysFrequentist  >>${YEAR}.log



exit

#combineTool.py -M Impacts -d $DC -m 125 -n$1  --setParameters mask_ch2_${SIGNAL}=0,mask_ch2_${SIDE}=0,r=1 --doInitialFit --robustFit 1  >${1}.impact.log
 
#combineTool.py -M Impacts -d $DC -m 125 -n$1 --setParameters mask_ch2_${SIGNAL}=0,mask_ch2_${SIDE}=0,r=1 --robustFit 1 --doFits   --parallel 50 >>${1}.impact.log

#combineTool.py -M Impacts -d $DC -m 125 -n$1 -o impacts${1}.json  >>${1}.impact.log

#plotImpacts.py -i impacts${1}.json -o impacts${1} >>${1}.impact.log

DC=higgsCombine${1}.MultiDimFit.mH120.root

#combineTool.py -M Impacts -d $DC -m 125 -n$1 --setParameters mask_ch1_${ZCONTROL}=1,mask_ch2_${SIGNAL}=0,mask_ch2_${SIDE}=0,r=1 --doInitialFit --robustFit 1 --cminDefaultMinimizerStrategy 0  >${1}.impact.log
#combineTool.py -M Impacts -d $DC -m 125 -n$1 --setParameters mask_ch1_${ZCONTROL}=1,mask_ch2_${SIGNAL}=0,mask_ch2_${SIDE}=0,r=1 --robustFit 1 --doFits --cminDefaultMinimizerStrategy 0  --parallel 50 >>${1}.impact.log
#combineTool.py -M Impacts -d $DC -m 125 -n$1 -o impacts${1}.json  >>${1}.impact.log
#plotImpacts.py -i impacts${1}.json -o impacts${1} >>${1}.impact.log
combineTool.py -M Impacts --snapshotName MultiDimFit -d $DC -m 125 -t -1  -n$1 --setParameters mask_ch1_${ZREGION}=$NoZ,mask_ch1_${ZCONTROL}=1,mask_ch2_${SIGNAL}=0,mask_ch2_${SIDE}=0,r=1 --doInitialFit --robustFit 1  --toysFrequentist >${1}.impact.log
combineTool.py -M Impacts --snapshotName MultiDimFit -d $DC -m 125 -t -1 -n$1 --setParameters mask_ch1_${ZREGION}=$NoZ,mask_ch1_${ZCONTROL}=1,mask_ch2_${SIGNAL}=0,mask_ch2_${SIDE}=0,r=1 --robustFit 1 --doFits --toysFrequentist  --parallel 50 >>${1}.impact.log
combineTool.py -M Impacts --snapshotName MultiDimFit -d $DC -m 125 -t -1 -n$1 -o impacts${1}.json --toysFrequentist -T 1500 >>${1}.impact.log
plotImpacts.py -i impacts${1}.json -o impacts${1} >>${1}.impact.log


 
combineTool.py -M FitDiagnostics -m 125 -d datacard${1}.root --there --cminDefaultMinimizerStrategy 0 --saveWorkspace --setParameters mask_ch1_${ZREGION}=$NoZ,mask_ch1_${ZCONTROL}=1,mask_ch2_${SIGNAL}=1,mask_ch2_${SIDE}=0,r=1 -n${1}  
PostFitShapesFromWorkspace -d datacard${1}.txt -w datacard${1}.root -o shapes${1}.root --print --postfit --sampling --freeze r=1. -f fitDiagnostics${1}.root:fit_s 
fi




python ./postFitPlot.py --year ${1} --file=shapes${1}.root --ratio --extra_pad=0.43   --ratio_range 0.4,1.6 --empty_bin_error --channel=ch1 --outname ${ZREGION}  --mode postfit --log_y --custom_y_range --y_axis_min "1E+1"  --channel_label "VBF Hmm" --file_dir ch1_${ZREGION}_postfit

cp ${ZREGION}_shapes${1}_postfit_logy.png  ../figure/${1}/
python ./postFitPlot.py  --year ${1} --file=shapes${1}.root --ratio --extra_pad=0.43   --ratio_range 0.4,1.6 --empty_bin_error --channel=ch1 --outname ${ZCONTROL}  --mode postfit --log_y --custom_y_range --y_axis_min "1E+1"  --channel_label "VBF Hmm" --file_dir ch1_${ZCONTROL}_postfit --y_title "pT balance"
cp ${ZCONTROL}_shapes${1}_postfit_logy.png  ../figure/${1}/

python ./postFitPlot.py --year ${1}  --file=shapes${1}.root --ratio --extra_pad=0.43   --ratio_range 0.4,1.6 --empty_bin_error --channel=ch2 --outname ${SIDE}  --mode postfit --log_y --custom_y_range --y_axis_min "1E-1"  --channel_label "VBF Hmm" --file_dir ch2_${SIDE}_postfit
cp ${SIDE}_shapes${1}_postfit_logy.png ../figure/$1/
python ./postFitPlot.py  --year ${1} --file=shapes${1}.root --ratio --extra_pad=0.43   --ratio_range 0.4,1.6 --empty_bin_error --channel=ch2 --outname ${SIGNAL}  --mode postfit --log_y --custom_y_range --y_axis_min "1E-2"  --channel_label "VBF Hmm" --file_dir ch2_${SIGNAL}_postfit   --blind --x_blind_min 2.0  --x_blind_max 4.0
cp ${SIGNAL}_shapes${1}_postfit_logy.png ../figure/$1/
 


python ./postFitPlot.py  --year ${1} --file=shapes${1}.root --ratio --extra_pad=0.43   --ratio_range 0.4,1.6 --empty_bin_error --channel=ch1 --outname ${ZREGION}  --mode prefit --log_y --custom_y_range --y_axis_min "1E+1"  --channel_label "VBF Hmm" --file_dir ch1_${ZREGION}_prefit

cp ${ZREGION}_shapes${1}_prefit_logy.png  ../figure/${1}/
python ./postFitPlot.py  --year ${1} --file=shapes${1}.root --ratio --extra_pad=0.43   --ratio_range 0.4,1.6 --empty_bin_error --channel=ch1 --outname ${ZCONTROL}  --mode prefit --log_y --custom_y_range --y_axis_min "1E+1"  --channel_label "VBF Hmm" --file_dir ch1_${ZCONTROL}_prefit --y_title "pT balance"
cp ${ZCONTROL}_shapes${1}_prefit_logy.png  ../figure/${1}/

python ./postFitPlot.py  --year ${1} --file=shapes${1}.root --ratio --extra_pad=0.43   --ratio_range 0.4,1.6 --empty_bin_error --channel=ch2 --outname ${SIDE}  --mode prefit --log_y --custom_y_range --y_axis_min "1E-1"  --channel_label "VBF Hmm" --file_dir ch2_${SIDE}_prefit
cp ${SIDE}_shapes${1}_prefit_logy.png ../figure/$1/
python ./postFitPlot.py  --year ${1} --file=shapes${1}.root --ratio --extra_pad=0.43   --ratio_range 0.4,1.6 --empty_bin_error --channel=ch2 --outname ${SIGNAL}  --mode prefit --log_y --custom_y_range --y_axis_min "1E-2"  --channel_label "VBF Hmm" --file_dir ch2_${SIGNAL}_prefit   --blind --x_blind_min 2.0  --x_blind_max 4.0
cp ${SIGNAL}_shapes${1}_prefit_logy.png ../figure/$1/


