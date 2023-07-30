cd ../code
for ID in $(seq 0 $1)
do
    python3 split.py $ID 6 4
done