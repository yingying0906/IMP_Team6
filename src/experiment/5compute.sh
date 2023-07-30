cd ../code

for ID in $(seq 0 $1)
do
    python3 computation.py $ID
done

