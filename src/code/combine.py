import random
import sys
import os 
import shamirs
import pickle

# change cwd
os.chdir("..")

# Get argument
target_ID = sys.argv[1]
target = sys.argv[2] # retrive which number
pick = int(sys.argv[3]) # pick how many shares  

# list
file_list = []

# Count total number of DB
num_shares = len(next(os.walk("database"))[1])
for i in range(num_shares):
    file_list.append(i)

# Randomly pick files in DB
pick_num = random.sample(range(0, len(file_list)), pick)
pick_list = []
for i in pick_num:
    with open(f"database/DB_{i}/{target_ID}_{target}_share_{i}","rb") as f:
        pick_list.append(pickle.load(f))

# Combine them
combine_s = shamirs.interpolate(pick_list)

# Write the combined file to "combine"
if not os.path.exists("combine"):
    os.makedirs("combine")
with open(f"combine/{target_ID}_combined_{target}", "wb") as f:
    pickle.dump(combine_s, f)

# Terminal
print(f"[ ID {target_ID} ] The shares of {target} are combined")