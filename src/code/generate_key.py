import lib
import os
import pickle

# change cwd
os.chdir("..")

# Generate Key
public_key, private_key = lib.getKey()

# Write Key
if not os.path.exists("key"):
    os.makedirs("key")
with open("key/public","wb") as f:
    pickle.dump(public_key, f)
with open("key/private","wb") as f:
    pickle.dump(private_key, f)

print(f" Keys are generated ")