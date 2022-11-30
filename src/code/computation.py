import paillier_calculation as pc
import sys
import pickle
import lib
import os

# change cwd
os.chdir("..")

# Get argument
target_ID = sys.argv[1]
encrypted_data_list = []

# Open the combined file

with open(f"combine/{target_ID}_combined_GOT","rb") as f:
    encrypted_data_list.append(pickle.load(f))
with open(f"combine/{target_ID}_combined_GPT","rb") as f:
    encrypted_data_list.append(pickle.load(f))

# get the keys
with open("key/public","rb") as f:
    public_key = pickle.load(f)
with open("key/private","rb") as f:
    private_key = pickle.load(f)

# Calculation
encrypted_result = pc.GOT_GPT_calc(encrypted_data_list, public_key)

# Terminal
decrypted_result = [private_key.decrypt(x) for x in encrypted_result]
print(f"[ ID {target_ID} ]")
print(str(decrypted_result))