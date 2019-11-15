export VAR1_H=DNN18Atan___SignalRegion
export VAR2_H=DNN18AtanNoMass___SideBand
export VAR1_Z=DNNZAtan___ZRegion
#export VAR2_Z=DNN18AtanNoMass___ZRegion
export VAR2_Z=pTbalanceAll___ZRegion

python plot.py models2018H -f outGiulio3// -v $VAR1_H $VAR2_H  -o figure_Andrea/ >& log2018H &
python plot.py models2018Z -f outGiulio3// -v $VAR1_Z $VAR2_Z  -o figure_Andrea/ >&  log2018Z &

python plot.py models2017H -f outGiulio3//  -v $VAR1_H $VAR2_H  -o figure_Andrea/ >& log2017H &
python plot.py models2017Z -f outGiulio3// -v $VAR1_Z $VAR2_Z  -o figure_Andrea/ >& log2017Z &

python plot.py models2016H -f outGiulio3//  -v $VAR1_H $VAR2_H  -o figure_Andrea/ >& log2016H &
python plot.py models2016Z -f outGiulio3// -v $VAR1_Z $VAR2_Z  -o figure_Andrea/ >& log2016Z &

python plot.py modelsAllH -f outGiulio3//  -v $VAR1_H $VAR2_H  -o figure_Andrea/ >& logAllH &
python plot.py modelsAllZ -f outGiulio3// -v $VAR1_Z $VAR2_Z  -o figure_Andrea/ >& logAllZ &


#python plot.py models2018H -f /scratch/arizzi/hmmNail/nail/PisaHmmSilvio/outFSR_lowstat17noPUnew_18tofixPtNom/  -v $VAR1_H $VAR2_H  -o figure_Andrea/ >& log2018H &
#python plot.py models2018Z -f /scratch/arizzi/hmmNail/nail/PisaHmmSilvio/outFSR_lowstat17noPUnew_18tofixPtNom/ -v $VAR1_Z $VAR2_Z  -o figure_Andrea/ >&  log2018Z &


#python plot.py models2017H -f /scratch/arizzi/hmmNail/nail/PisaHmmSilvio/outFSR_lowstat17noPUnew_18tofixPtNom/  -v $VAR1_H $VAR2_H  -o figure_Andrea/ >& log2017H &
#python plot.py models2017Z -f /scratch/arizzi/hmmNail/nail/PisaHmmSilvio/outFSR_lowstat17noPUnew_18tofixPtNom/ -v $VAR1_Z $VAR2_Z  -o figure_Andrea/ >& log2017Z &


#python plot.py models2016H -f /scratch/arizzi/hmmNail/nail/PisaHmmSilvio/out2016/  -v $VAR1_H $VAR2_H  -o figure_Andrea/ >& log2016H &
#python plot.py models2016Z -f /scratch/arizzi/hmmNail/nail/PisaHmmSilvio/out2016/ -v $VAR1_Z $VAR2_Z  -o figure_Andrea/ >& log2016Z &


