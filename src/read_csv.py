import numpy as np
import sys
import csv
import os

# argument
filename = sys.argv[1]
num = int(sys.argv[2])

# open folder
if not os.path.exists(f"./data/{filename[:-4]}"):
    os.makedirs(f"./data/{filename[:-4]}")

# open csv
with open(filename,'r') as f:
    reader = csv.reader(f)

    # Get Header
    header = next(reader)
    pick_list = []
    for i in range(len(header)):
        if header[i] == "ID":
            pick_list.append(i)
        if header[i] == "GPT":
            pick_list.append(i)
        if header[i] == "GOT":
            pick_list.append(i)
    
    # Get 100 patients data
    for rows in reader:
        # break statement
        if(int(rows[0]) == num+1):
            break
        #print(rows)

        # open file
        with open(f"data/{filename[:-4]}/{rows[0]}", 'w') as f:
            # Take the targeted header data
            for i in pick_list:
                data = []
                data.append(header[i])
                data.append(rows[i])
                f.write(f"{data[0]} {data[1]}\n")
            
            

        
        