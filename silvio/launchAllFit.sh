#DNNZAtan___ZRegion
#DNN18AtanNoMass___ZRegion
#DNN18Atan___SignalRegion
#DNN18AtanNoMass___SideBand


python makeScript.py \
--steps makeDC,significance_asimov,significance_prefit,significance_fit,postFitPlot_prefit,postFitPlot_fit,impacts_asimov,impacts_prefit,impacts_fit \
--directory workspace_new_fitZ_DNNZ \
--years 2016,2017,2018,All,Comb \
--fitPlots      DNNZAtan___ZRegion,DNN18AtanNoMass___SideBand \
--prefitPlots   DNN18AtanNoMass___SideBand \
--fitOptions "--cminDefaultMinimizerStrategy 0" \
--fitZ \
--nprocesses 10 \
>& logFitZ_DNNZ &

python makeScript.py \
--steps makeDC,significance_asimov,significance_prefit,significance_fit,postFitPlot_prefit,postFitPlot_fit,impacts_asimov,impacts_prefit,impacts_fit \
--directory workspace_new_fitZ_classic \
--years 2016,2017,2018,All,Comb \
--fitPlots      DNN18AtanNoMass___ZRegion,DNN18AtanNoMass___SideBand \
--prefitPlots   DNN18AtanNoMass___SideBand \
--fitOptions "--cminDefaultMinimizerStrategy 0" \
--fitZ \
--nprocesses 10 \
>& logFitZ_classic &

python makeScript.py \
--steps makeDC,significance_asimov,significance_prefit,postFitPlot_prefit,impacts_asimov,impacts_prefit,impacts_fit \
--directory workspace_new_fitH_classic \
--years 2016,2017,2018,All,Comb \
--fitPlots      DNN18AtanNoMass___ZRegion,DNN18AtanNoMass___SideBand,DNN18Atan___SignalRegion \
--prefitPlots   DNN18AtanNoMass___ZRegion,DNN18AtanNoMass___SideBand \
--fitOptions "--cminDefaultMinimizerStrategy 0" \
--fitH \
--nprocesses 10 \
>& logFitH_classic &

python makeScript.py \
--steps makeDC,significance_asimov,significance_prefit,postFitPlot_prefit,impacts_asimov,impacts_prefit,impacts_fit \
--directory workspace_new_fitH_DNNZ \
--years 2016,2017,2018,All,Comb \
--fitPlots      DNNZAtan___ZRegion,DNN18AtanNoMass___SideBand,DNN18Atan___SignalRegion \
--prefitPlots   DNNZAtan___ZRegion,DNN18AtanNoMass___SideBand \
--fitOptions "--cminDefaultMinimizerStrategy 0" \
--fitH \
--nprocesses 10 \
>& logFitH_DNNZ &
