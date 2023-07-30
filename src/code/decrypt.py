import lib
import sys
import pickle
import os

# change cwd
os.chdir("..")

# Get argument
patient_ID = sys.argv[1]
header = sys.argv[2]

# list
combine_list = []

# Open combined file

with open(f"combine/{patient_ID}_combined_{header}", "rb") as f:
    combine_list.append(pickle.load(f))

# Open key files
with open("key/public", "rb") as f:
    public_key = pickle.load(f)
with open("key/private", "rb") as f:
    private_key = pickle.load(f)

# Decrypted
decrypted_number_list = lib.getDecryptedNumber(combine_list, public_key, private_key) 

# Terminal
#print(f"[ patient_ID {patient_ID} ] {header} is ", end = '')
#for number in decrypted_number_list:
    #print(number)