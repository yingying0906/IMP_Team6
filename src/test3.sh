cd code

# generate key
python3 generate_key.py

cd ..

# add data to the db
for patient in $(seq 0 $2)
do
    sh add.sh -i $patient -t 4 -n 6 -p $1
done

# combine data to the db
for patient in $(seq 0 $2)
do
    sh get.sh -i $patient -t 4 -h GOT
    sh get.sh -i $patient -t 4 -h GPT
done

# cal data to the db
for patient in $(seq 0 $2)
do
    sh cal.sh -i $patient
done