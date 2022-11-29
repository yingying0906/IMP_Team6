import numpy as np
import sys
import csv

# change cwd
os.chdir("..")

filename = sys.argv[1]
with open(filename,'r') as f:
    reader = csv.reader(f)
    ID = 0
    for row in reader:
        if(ID < 100):
            GPT = row[5]
            GOT = row[6]
            ID += 1
            with open('./data/p_'+ str(ID),'w') as out_f:
                out_f.write(str(ID) + ' ' + str(GPT) + ' ' + str(GOT))
        else:
            break
        