cd code

# encrypt
python3 encrypt.py 1
python3 encrypt.py 2

# split
python3 split.py 1 6 3
python3 split.py 2 6 3

# combine and decrypt GOT in 7 share
python3 combine.py 1 GPT 3
python3 decrypt.py 1 GPT

# combine and decrypt GOT in 5 share (fail)
python3 combine.py 2 GOT 4
python3 decrypt.py 2 GOT
