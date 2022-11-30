import lib
import sys
import pickle
import os

# change cwd
os.chdir("..")

# argument
filename = sys.argv[1]

# list
secret_number_list = []
header_list = []

# Open file
if not os.path.exists("./data"):
    os.makedirs("./data")

with open("data/" + filename,"r") as f:
    fr = f.read()
    byline = fr.split("\n")
    for i in byline:
        byspace = i.split(" ")
        if(byspace[0] == "ID"):
            ID = byspace[1]
        else:
            header_list.append(byspace[0])
            secret_number_list.append(int(byspace[1]))

# Get Key
with open("key/public","rb") as f:
    public_key = pickle.load(f)
with open("key/private","rb") as f:
    private_key = pickle.load(f)

# Encrypt
encrypted_number_list = lib.getEncryptedNumber(secret_number_list, public_key)

# Write
if not os.path.exists("./temp"):
    os.makedirs("./temp")
with open("temp/" + ID +"_encrypted","wb") as f:
    pickle.dump(encrypted_number_list, f)
with open("temp/" + ID +"_header","wb") as f:
    pickle.dump(header_list, f)

# print(f"there are {len(encrypted_number_list)} numbers and their type is {type(encrypted_number_list[0])}")
print(f"[ ID {filename} ] {len(encrypted_number_list)} numbers is encrypted")