import random
import lib
import shamirs
import sys
import os
import pickle

# change cwd
os.chdir("..")

# open file
target_ID = sys.argv[1]
with open("temp/" + target_ID + "_encrypted","rb") as f:
    encrypted_number_list = pickle.load(f)
with open("temp/" + target_ID + "_header","rb") as f:
    header_list = pickle.load(f)

# split
N, T = int(sys.argv[2]), int(sys.argv[3])
shares_list = []

for i in encrypted_number_list:
    shares_list.append(shamirs.shares(i, quantity=N, threshold=T, modulus=lib.MODULUS))

# create DB folder
if not os.path.exists("./database"):
    os.makedirs("./database")
for i in range(N):
    if not os.path.exists("./database/DB_" + str(i)):
        os.makedirs("./database/DB_" + str(i))

# write
for i in range(N):
    path1 = "database/DB_" + str(i) + "/" + target_ID + "_"
    for j in range(len(shares_list)):
        path2 = path1 + header_list[j] + "_share_" + str(i)
        with open(path2, "wb") as f:
            pickle.dump(shares_list[j][i], f)

print(f"[ ID {target_ID} ] The data is splitted into {N} shares with threshold {T}") 