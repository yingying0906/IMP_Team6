cd ../code

for ID in $(seq 0 $1)
do
    python3 encrypt.py patient_dataset $ID 
done