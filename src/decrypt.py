import lib
import sys
import pickle
import os

# argument
target_ID = sys.argv[1]
target = sys.argv[2]

# list
combine_list = []

# open combined file
with open("combine/" + target_ID + "_combined_" + target, "rb") as f:
    combine_list.append(pickle.load(f))

# open key
with open("key/public", "rb") as f:
    public_key = pickle.load(f)
with open("key/private", "rb") as f:
    private_key = pickle.load(f)

# Decrypted
decrypted_number_list = lib.getDecryptedNumber(combine_list, public_key, private_key) # the type of each item in encrypted_number_list should be 'int'

# print(f'there are {len(decrypted_number_list)} numbers and the value is below:')
print(f"[ ID {target_ID} ] {target} is ", end = '')
for number in decrypted_number_list:
    print(number)