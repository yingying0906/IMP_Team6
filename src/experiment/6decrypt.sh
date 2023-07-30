cd ../code

for ID in $(seq 0 $1)
do
    python3 decrypt.py $ID $2
done
