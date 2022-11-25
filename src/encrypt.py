import lib
import sys
import pickle

# list
secret_number_list = []
filename = sys.argv[1]

# Open file
with open("data/" + filename,"r") as f:
    fr = f.read()
    s = fr.split(" ")
    for i in s:
        secret_number_list.append(int(i))

# Generate Key
public_key, private_key = lib.getKey()

# Write Key
with open("temp/public","wb") as f:
    pickle.dump(public_key, f)
with open("temp/private","wb") as f:
    pickle.dump(private_key, f)

# Encrypt
encrypted_number_list = lib.getEncryptedNumber(secret_number_list, public_key)

# Write
with open("temp/encrypted","wb") as f:
    pickle.dump(encrypted_number_list, f)

print(f"there are {len(encrypted_number_list)} numbers and their type is {type(encrypted_number_list[0])}")