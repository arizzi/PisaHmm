#!/bin/bash

DIR1="workspace_new_fitZ_DNNZ"
DIR2="workspace_new_fitH_DNNZ"
DIR3="workspace_new_fitZ_classic"
DIR4="workspace_new_fitH_classic"

AFSDIR="/afs/pi.infn.it/user/sdonato/public_html/Hmm"

for DIR in $DIR1 $DIR2 $DIR3 $DIR4; do
    echo mkdir -p $AFSDIR"/"$DIR
    echo cp $DIR1/*pdf $AFSDIR/$DIR
    echo cp $DIR1/*png $AFSDIR/$DIR
    echo cp $DIR1/*sh $AFSDIR/$DIR
#    echo cp $DIR1/*log $AFSDIR/$DIR
    mkdir -p $AFSDIR"/"$DIR
    cp $DIR1/*pdf $AFSDIR/$DIR
    cp $DIR1/*png $AFSDIR/$DIR
    cp $DIR1/*sh $AFSDIR/$DIR
#    cp $DIR1/*log $AFSDIR/$DIR
done
