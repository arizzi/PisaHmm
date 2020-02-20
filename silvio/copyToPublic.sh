#!/bin/bash

DIR1="workspace_new_fitZ_DNNZ"
DIR2="workspace_new_fitH_DNNZ"
DIR3="workspace_new_fitZ_classic"
DIR4="workspace_new_fitH_classic"

AFSDIR="/afs/pi.infn.it/user/sdonato/public_html/Hmm"
INDEXPHP="/afs/pi.infn.it/user/arizzi/public_html/nov21/2017/index.php"

for DIR in $DIR1 $DIR2 $DIR3 $DIR4; do
    echo mkdir -p $AFSDIR"/"$DIR
    echo cp $DIR/*pdf $AFSDIR/$DIR
    echo cp $DIR/*png $AFSDIR/$DIR
    echo cp $DIR/*sh $AFSDIR/$DIR
#    echo cp $DIR/*log $AFSDIR/$DIR
    mkdir -p $AFSDIR"/"$DIR
    cp $DIR/*pdf $AFSDIR/$DIR
    cp $DIR/*png $AFSDIR/$DIR
    cp $DIR/*sh $AFSDIR/$DIR
    cp models*py $AFSDIR/$DIR
    cp $INDEXPHP $AFSDIR/$DIR
#    cp $DIR/*log $AFSDIR/$DIR
done
