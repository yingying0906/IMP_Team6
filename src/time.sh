#!/bin/bash

cd code

for N in {3..10}
do
    for M in $(seq 2 $N)
    do 
        start=$(date +%s.%N)
        python3 split.py 1 ${N} ${M} 
        end=$(date +%s.%N)
        runtime=$(python3 -c "print(${end} - ${start})")
        echo "split $N $M $runtime"

        for T in $(seq $M $N)
        do 
            start=$(date +%s.%N)
            python3 combine.py 1 GPT ${T} 
            python3 combine.py 1 GOT ${T} 
            end=$(date +%s.%N)
            runtime=$(python3 -c "print(${end} - ${start})")
            echo "combine $N $T $runtime"
        done
    done
done
