#DNNZAtan___ZRegion
#DNN18AtanNoMass___ZRegion
#DNN18Atan___SignalRegion
#DNN18AtanNoMass___SideBand


python makeFitScript.py \
--steps makeDC,significance_asimov,significance_partialfit,significance_fullfit,postFitPlot_partialfit,postFitPlot_fullfit,impacts_asimov,impacts_partialfit,impacts_fullfit \
--directory workspacefitZ_DNNZ \
--inputDirectory workspace \
--years 2016,2017,2018,All,Comb \
--fullfitPlots      DNNZAtan___ZRegion,DNN18AtanNoMass___SideBand \
--partialfitPlots   DNN18AtanNoMass___SideBand \
--fitOptions "--cminDefaultMinimizerStrategy 0" \
--fitZ \
--nprocesses 10 \
--verbose 10 \
>& logFitZ_DNNZ &

python makeFitScript.py \
--steps makeDC,significance_asimov,significance_partialfit,significance_fullfit,postFitPlot_partialfit,postFitPlot_fullfit,impacts_asimov,impacts_partialfit,impacts_fullfit \
--directory workspacefitZ_classic \
--inputDirectory workspace \
--years 2016,2017,2018,All,Comb \
--fullfitPlots      DNN18AtanNoMass___ZRegion,DNN18AtanNoMass___SideBand \
--partialfitPlots   DNN18AtanNoMass___SideBand \
--fitOptions "--cminDefaultMinimizerStrategy 0" \
--fitZ \
--nprocesses 10 \
--verbose 10 \
>& logFitZ_classic &

python makeFitScript.py \
--steps makeDC,significance_asimov,significance_partialfit,postFitPlot_partialfit,impacts_asimov,impacts_partialfit,impacts_fullfit \
--directory workspacefitH_classic \
--inputDirectory workspace \
--years 2016,2017,2018,All,Comb \
--fullfitPlots      DNN18AtanNoMass___ZRegion,DNN18AtanNoMass___SideBand,DNN18Atan___SignalRegion \
--partialfitPlots   DNN18AtanNoMass___ZRegion,DNN18AtanNoMass___SideBand \
--fitOptions "--cminDefaultMinimizerStrategy 0" \
--fitH \
--nprocesses 10 \
--verbose 10 \
>& logFitH_classic &

python makeFitScript.py \
--steps makeDC,significance_asimov,significance_partialfit,postFitPlot_partialfit,impacts_asimov,impacts_partialfit,impacts_fullfit \
--directory workspacefitH_DNNZ \
--inputDirectory workspace \
--years 2016,2017,2018,All,Comb \
--fullfitPlots      DNNZAtan___ZRegion,DNN18AtanNoMass___SideBand,DNN18Atan___SignalRegion \
--partialfitPlots   DNNZAtan___ZRegion,DNN18AtanNoMass___SideBand \
--fitOptions "--cminDefaultMinimizerStrategy 0" \
--fitH \
--nprocesses 10 \
--verbose 10 \
>& logFitH_DNNZ &
