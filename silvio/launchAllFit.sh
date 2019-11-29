#DNNZAtan___ZRegion
#DNN18AtanNoMass___ZRegion
#DNN18Atan___SignalRegion
#DNN18AtanNoMass___SideBand

python makeScript.py \
--steps makeDC,significance_asimov,significance_prefit,significance_fit,postFitPlot_prefit,postFitPlot_fit,impacts_asimov,impacts_prefit,impacts_fit \
--directory workspaceTest2 \
--years 2016 \
--fitPlots      DNNZAtan___ZRegion,DNN18AtanNoMass___SideBand \
--prefitPlots   DNN18AtanNoMass___SideBand \
--fitOptions "--cminDefaultMinimizerStrategy 0 --robustFit 1" \
--fitZ \
--nprocesses 10

