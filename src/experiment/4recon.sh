cd ../code

for ID in $(seq 0 $1)
do
    python3 combine.py $ID $2 4
done