import random
import sys
import os 
import shamirs
import pickle

num = int(sys.argv[1]) # retrive which number
pick = int(sys.argv[2]) # pick how many shares  
file_list = []

# Read all filename
for filename in os.listdir("share/" + str(num)):
        file_list.append(filename)

# randomly pick files
pick_num = random.sample(range(0, len(file_list)), 5)
pick_list = []
for i in pick_num:
    path = "share/" + str(num) + "/" + "share_" + str(i)
    with open(path,"rb") as f:
        pick_list.append(pickle.load(f))

# combine 
combine_s = shamirs.interpolate(pick_list)

# write
with open("temp/combined_" + str(num), "w") as f:
    f.write(str(combine_s))

print(f"The shares are combined")