import random
import sys
import os 
import shamirs
import pickle

# change cwd
os.chdir("..")

# argument
target_ID = sys.argv[1]
target = sys.argv[2] # retrive which number
pick = int(sys.argv[3]) # pick how many shares  

# list
file_list = []

# Read all filename
num_shares = len(next(os.walk("database"))[1])
for i in range(num_shares):
    file_list.append(i)

# randomly pick files
pick_num = random.sample(range(0, len(file_list)), pick)
pick_list = []
for i in pick_num:
    path = "database/DB_" + str(i) + "/" + target_ID + "_" + target + "_share_" + str(i)
    with open(path,"rb") as f:
        pick_list.append(pickle.load(f))

# combine 
combine_s = shamirs.interpolate(pick_list)

# write
if not os.path.exists("combine"):
    os.makedirs("combine")
with open("combine/" + target_ID + "_combined_" + target, "wb") as f:
    pickle.dump(combine_s, f)
    
print(f"[ ID {target_ID} ] The shares of {target} are combined")