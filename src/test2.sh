cd code

# generate key
python3 generate_key.py

cd ..

# add to the DB
sh add.sh 1 10 6
sh add.sh 2 10 6

# get from the DB
sh get.sh 1 GPT 6
sh get.sh 1 GOT 7
sh get.sh 2 GPT 8
sh get.sh 2 GOT 9

# calculate them
sh cal.sh 1
sh cal.sh 2