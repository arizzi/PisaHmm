#!/bin/bash
ZREGION=DNNAtanNoMass___ZRegion
ZCONTROL=pTbalanceAll___ZRegion
SIGNAL=DNNAtan___SignalRegion
SIDE=DNNAtanNoMass___SideBand
if /bin/true ; then 
combineCards.py datacard${1}Z.txt datacard${1}H.txt > datacard${1}.txt 2> ${1}.log
text2workspace.py -P HiggsAnalysis.CombinedLimit.PhysicsModel:multiSignalModel    --channel-masks datacard${1}.txt   --PO  'map=.*Hmm.*:r[1.,-10,10]'  >>${1}.log

combine  -M MultiDimFit -n$1 --saveWorkspace --setParameters mask_ch1_${ZCONTROL}=1,mask_ch2_${SIGNAL}=1,mask_ch2_${SIDE}=0 datacard${1}.root --verbose 9   --robustFit 1 >>${1}.log

combine -M Significance --snapshotName MultiDimFit -t -1  higgsCombine${1}.MultiDimFit.mH120.root --setParameters mask_ch1_${ZCONTROL}=1,mask_ch2_${SIGNAL}=0,mask_ch2_${SIDE}=0,r=1   >>${1}.log
combine -M Significance --snapshotName MultiDimFit -t -1  higgsCombine${1}.MultiDimFit.mH120.root --setParameters mask_ch1_${ZCONTROL}=1,mask_ch2_${SIGNAL}=0,mask_ch2_${SIDE}=0,r=1  --toysFrequentist  >>${1}.log
DC=higgsCombine${1}.MultiDimFit.mH120.root


#combineTool.py -M Impacts -d $DC -m 125 -n$1  --setParameters mask_ch2_${SIGNAL}=0,mask_ch2_${SIDE}=0,r=1 --doInitialFit --robustFit 1  >${1}.impact.log
 
#combineTool.py -M Impacts -d $DC -m 125 -n$1 --setParameters mask_ch2_${SIGNAL}=0,mask_ch2_${SIDE}=0,r=1 --robustFit 1 --doFits   --parallel 50 >>${1}.impact.log

#combineTool.py -M Impacts -d $DC -m 125 -n$1 -o impacts${1}.json  >>${1}.impact.log

#plotImpacts.py -i impacts${1}.json -o impacts${1} >>${1}.impact.log

DC=higgsCombine${1}.MultiDimFit.mH120.root
combineTool.py -M Impacts -d $DC -m 125 -n$1 --setParameters mask_ch1_${ZCONTROL}=1,mask_ch2_${SIGNAL}=0,mask_ch2_${SIDE}=0,r=1 --doInitialFit --robustFit 1  >${1}.impact.log
combineTool.py -M Impacts -d $DC -m 125 -n$1 --setParameters mask_ch1_${ZCONTROL}=1,mask_ch2_${SIGNAL}=0,mask_ch2_${SIDE}=0,r=1 --robustFit 1 --doFits   --parallel 50 >>${1}.impact.log
combineTool.py -M Impacts -d $DC -m 125 -n$1 -o impacts${1}.json  >>${1}.impact.log


 
combineTool.py -M FitDiagnostics -m 125 -d datacard${1}.root --there --cminDefaultMinimizerStrategy 0 --saveWorkspace --setParameters mask_ch1_${ZCONTROL}=1,mask_ch2_${SIGNAL}=1,mask_ch2_${SIDE}=0,r=1 
PostFitShapesFromWorkspace -d datacard${1}.txt -w datacard${1}.root -o shapes${1}.root --print --postfit --sampling --freeze r=1. -f fitDiagnostics.Test.root:fit_s
fi
python ./postFitPlot.py --file=shapes${1}.root --ratio --extra_pad=0.43   --ratio_range 0.4,1.6 --empty_bin_error --channel=ch1 --outname ${ZREGION}  --mode postfit --log_y --custom_y_range --y_axis_min "1E+1"  --channel_label "VBF Hmm" --file_dir ch1_${ZREGION}_postfit

cp ${ZREGION}_shapes${1}_postfit_logy.png  ../figure/${1}/
python ./postFitPlot.py --file=shapes${1}.root --ratio --extra_pad=0.43   --ratio_range 0.4,1.6 --empty_bin_error --channel=ch1 --outname ${ZCONTROL}  --mode postfit --log_y --custom_y_range --y_axis_min "1E+1"  --channel_label "VBF Hmm" --file_dir ch1_${ZCONTROL}_postfit
cp ${ZCONTROL}_shapes${1}_postfit_logy.png  ../figure/${1}/

python ./postFitPlot.py --file=shapes${1}.root --ratio --extra_pad=0.43   --ratio_range 0.4,1.6 --empty_bin_error --channel=ch2 --outname ${SIDE}  --mode postfit --log_y --custom_y_range --y_axis_min "1E-1"  --channel_label "VBF Hmm" --file_dir ch2_${SIDE}_postfit
cp ${SIDE}_shapes${1}_postfit_logy.png ../figure/$1/
python ./postFitPlot.py --file=shapes${1}.root --ratio --extra_pad=0.43   --ratio_range 0.4,1.6 --empty_bin_error --channel=ch2 --outname ${SIGNAL}  --mode postfit --log_y --custom_y_range --y_axis_min "1E-2"  --channel_label "VBF Hmm" --file_dir ch2_${SIGNAL}_postfit   --blind --x_blind_min 1.0  --x_blind_max 4.0
cp ${SIGNAL}_shapes${1}_postfit_logy.png ../figure/$1/
 

python ./postFitPlot.py --file=shapes${1}.root --ratio --extra_pad=0.43   --ratio_range 0.4,1.6 --empty_bin_error --channel=ch1 --outname ${ZREGION}  --mode prefit --log_y --custom_y_range --y_axis_min "1E+1"  --channel_label "VBF Hmm" --file_dir ch1_${ZREGION}_prefit

cp ${ZREGION}_shapes${1}_prefit_logy.png  ../figure/${1}/
python ./postFitPlot.py --file=shapes${1}.root --ratio --extra_pad=0.43   --ratio_range 0.4,1.6 --empty_bin_error --channel=ch1 --outname ${ZCONTROL}  --mode prefit --log_y --custom_y_range --y_axis_min "1E+1"  --channel_label "VBF Hmm" --file_dir ch1_${ZCONTROL}_prefit
cp ${ZCONTROL}_shapes${1}_prefit_logy.png  ../figure/${1}/

python ./postFitPlot.py --file=shapes${1}.root --ratio --extra_pad=0.43   --ratio_range 0.4,1.6 --empty_bin_error --channel=ch2 --outname ${SIDE}  --mode prefit --log_y --custom_y_range --y_axis_min "1E-1"  --channel_label "VBF Hmm" --file_dir ch2_${SIDE}_prefit
cp ${SIDE}_shapes${1}_prefit_logy.png ../figure/$1/
python ./postFitPlot.py --file=shapes${1}.root --ratio --extra_pad=0.43   --ratio_range 0.4,1.6 --empty_bin_error --channel=ch2 --outname ${SIGNAL}  --mode prefit --log_y --custom_y_range --y_axis_min "1E-2"  --channel_label "VBF Hmm" --file_dir ch2_${SIGNAL}_prefit   --blind --x_blind_min 1.0  --x_blind_max 4.0
cp ${SIGNAL}_shapes${1}_prefit_logy.png ../figure/$1/

