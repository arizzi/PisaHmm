export YEAR=2018
cd workspace_DNNZ_fewBins && ./doall4names.sh ${YEAR} >& logTestDF${YEAR} &
cd workspace_classic_fewBins && ./doall4names.sh ${YEAR} >& logTestCF${YEAR} &
cd workspace_DNNZ && ./doall4names.sh ${YEAR} >& logTest${YEAR}D &
cd workspace_classic && ./doall4names.sh ${YEAR} >& logTest${YEAR}C &
