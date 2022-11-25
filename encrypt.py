import phe_lib as phe
import sys

# list
secret_number_list = []
filename = sys.argv[1]
# Open file
with open("./data/" + filename,'r') as f:
    fr = f.read()
    s = fr.split(' ')
    for i in s:
        secret_number_list.append(int(i))

# Generate Key
public_key, private_key = phe.getKey()

# Encrypt
encrypted_number_list = phe.getEncryptedNumber(secret_number_list, public_key)

# Write
with open("./data/encrypted",'w') as f:
    f.write(str(encrypted_number_list))

print(f'there are {len(encrypted_number_list)} numbers and their type is {type(encrypted_number_list[0])}')