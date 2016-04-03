#!/bin/bash
#Usage: benchmark.sh <python script> [args to script]

trap ctrl_c INT

if [ -z $1 ] ; then
    echo "Usage: benchmark.sh <python script> [args to script]" > /dev/stderr
    exit 1
fi

function ctrl_c() {
    echo "Command: $pscript $pscript_args"
    echo "Games: $i"
    echo "2048:  $count2048"
    echo "1024:  $count1024"
    echo "512:  $count512"
    echo "256:  $count256"
    echo

    exit 0
}

pscript=$1
shift
pscript_args=$*

i=0
count2048=0
count1024=0
count512=0
count256=0
while : ; do
    ofile=`mktemp`
    python $pscript $pscript_args > $ofile

    if [ $? -ne 0 ]
    then
        echo "Some error" > /dev/stderr
        exit 2
    fi

    if grep 2048 $ofile > /dev/null 
    then
        let count2048+=1
        let count1024+=1
        let count512+=1
        let count256+=1
    elif grep 1024 $ofile > /dev/null 
    then
        let count1024+=1
        let count512+=1
        let count256+=1
    elif grep 512 $ofile > /dev/null 
    then
        let count512+=1
        let count256+=1
    elif grep 256 $ofile > /dev/null 
    then
        let count256+=1
    fi

    rm $ofile
    let i+=1
done
