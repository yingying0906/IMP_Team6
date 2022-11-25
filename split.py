import random
import ss_lib as ss
import shamirs
import sys
import os

# open file
encrypted_number_list = []
with open("./data/encrypted",'r') as f:
    res = f.read().strip('][').split(', ')
    for i in res:
        encrypted_number_list.append(int(i))

# split
N, T = int(sys.argv[1]), int(sys.argv[2])
shares_list = []

for i in encrypted_number_list:
    shares_list.append(shamirs.shares(i, quantity=N, threshold=T, modulus=ss.MODULUS))

# write
for i in range(len(shares_list)):
    path1 = "./share/" + str(i)
    if(os.path.exists(path1) == False):
        os.makedirs(path1)
    for j in range(len(shares_list[i])):
        path2 = path1 + "/share_" + str(j)
        with open(path2, 'w') as f:
            f.write(str(shares_list[i][j]))

print(f'The secret number is splitted into %d shares with threshold %d' % (N, T)) 