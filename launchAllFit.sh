#DNNZAtan___ZRegion
#DNN18AtanNoMass___ZRegion
#DNN18Atan___SignalRegion
#DNN18AtanNoMass___SideBand


python makeScript.py \
--steps makeDC,significance_asimov,significance_partialfit,significance_fullfit,postFitPlot_partialfit,postFitPlot_fullfit,impacts_asimov,impacts_partialfit,impacts_fullfit \
--directory workspace_test_fullfitZ_DNNZ \
--years 2016,2017,2018,All,Comb \
--fullfitPlots      DNNZAtan___ZRegion,DNN18AtanNoMass___SideBand \
--partialfitPlots   DNN18AtanNoMass___SideBand \
--fitOptions "--cminDefaultMinimizerStrategy 0" \
--fitZ \
--nprocesses 10 \
>& logFitZ_DNNZ &

python makeScript.py \
--steps makeDC,significance_asimov,significance_partialfit,significance_fullfit,postFitPlot_partialfit,postFitPlot_fullfit,impacts_asimov,impacts_partialfit,impacts_fullfit \
--directory workspace_test_fullfitZ_classic \
--years 2016,2017,2018,All,Comb \
--fullfitPlots      DNN18AtanNoMass___ZRegion,DNN18AtanNoMass___SideBand \
--partialfitPlots   DNN18AtanNoMass___SideBand \
--fitOptions "--cminDefaultMinimizerStrategy 0" \
--fitZ \
--nprocesses 10 \
>& logFitZ_classic &

python makeScript.py \
--steps makeDC,significance_asimov,significance_partialfit,postFitPlot_partialfit,impacts_asimov,impacts_partialfit,impacts_fullfit \
--directory workspace_test_fullfitH_classic \
--years 2016,2017,2018,All,Comb \
--fullfitPlots      DNN18AtanNoMass___ZRegion,DNN18AtanNoMass___SideBand,DNN18Atan___SignalRegion \
--partialfitPlots   DNN18AtanNoMass___ZRegion,DNN18AtanNoMass___SideBand \
--fitOptions "--cminDefaultMinimizerStrategy 0" \
--fitH \
--nprocesses 10 \
>& logFitH_classic &

python makeScript.py \
--steps makeDC,significance_asimov,significance_partialfit,postFitPlot_partialfit,impacts_asimov,impacts_partialfit,impacts_fullfit \
--directory workspace_test_fullfitH_DNNZ \
--years 2016,2017,2018,All,Comb \
--fullfitPlots      DNNZAtan___ZRegion,DNN18AtanNoMass___SideBand,DNN18Atan___SignalRegion \
--partialfitPlots   DNNZAtan___ZRegion,DNN18AtanNoMass___SideBand \
--fitOptions "--cminDefaultMinimizerStrategy 0" \
--fitH \
--nprocesses 10 \
>& logFitH_DNNZ &
