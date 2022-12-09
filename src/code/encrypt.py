import lib
import sys
import pickle
import os

# change cwd
os.chdir("..")

# Get argument
path = sys.argv[1]
filename = sys.argv[2]

# list
header_list = []
secret_number_list = []

# Make directory "data"
if not os.path.exists("./data"):
    os.makedirs("./data")

# Open data
with open(f"data/{path}/{filename}","r") as f:
    fr = f.read()
    byline = fr.split("\n") # split by newline
    for i in byline:
        byspace = i.split(" ") # split by space
        if(len(byspace) != 1):
            if(byspace[0] == "ID"):
                ID = byspace[1]
            else:
                header_list.append(byspace[0])
                secret_number_list.append(int(byspace[1]))

# Open Key files
with open("key/public","rb") as f:
    public_key = pickle.load(f)
with open("key/private","rb") as f:
    private_key = pickle.load(f)

# Encrypt
encrypted_number_list = lib.getEncryptedNumber(secret_number_list, public_key)

# Make directory "temp"
if not os.path.exists("./temp"):
    os.makedirs("./temp")

# Write encrypted data
with open(f"temp/{ID}_encrypted","wb") as f:
    pickle.dump(encrypted_number_list, f)

# Write the header of the encrypted data
with open(f"temp/{ID}_header","wb") as f:
    pickle.dump(header_list, f)

# Terminal
print(f"[ ID {filename} ] {len(encrypted_number_list)} numbers is encrypted")
print(encrypted_number_list)