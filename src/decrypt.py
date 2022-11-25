import lib
import sys
import pickle

filename = sys.argv[1]
combine_list = []

# open combined file
with open("temp/combined_" + filename, "r") as f:
    combine_list.append(int(f.read()))

# open key
with open("temp/public", "rb") as f:
    public_key = pickle.load(f)
with open("temp/private", "rb") as f:
    private_key = pickle.load(f)

# Decrypted
decrypted_number_list = lib.getDecryptedNumber(combine_list, public_key, private_key) # the type of each item in encrypted_number_list should be 'int'

print(f'there are {len(decrypted_number_list)} numbers and the value is below:')
for number in decrypted_number_list:
    print(number)