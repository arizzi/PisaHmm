#!/bin/bash
for y in 2016 2017 2018 ; do 
for i in `cat todecorrelate3.txt | grep -v \#` ; do 
 echo nuisance edit rename .\*$y.\* \* $i $i$y 
done

done
