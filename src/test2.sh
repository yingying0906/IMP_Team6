cd code

# generate key
python3 generate_key.py

cd ..

# add to the DB
sh add.sh -i 1 -t 4 -n 6
sh add.sh -i 2 -t 4 -n 6

# get from the DB
sh get.sh -i 1 -h GPT -t 4
sh get.sh -i 1 -h GOT -t 5
sh get.sh -i 2 -h GPT -t 6
sh get.sh -i 2 -h GOT -t 6

# calculate them
sh cal.sh -i 1
sh cal.sh -i 2