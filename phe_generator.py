# Download the pyphe package 
# using pip: 
# $ pip install phe

from phe import paillier
import shamirs
import random

def getKey(): # get public key and private key from pyphe package
    public_key, private_key = paillier.generate_paillier_keypair()
    keyring = paillier.PaillierPrivateKeyring()
    keyring.add(private_key)
    return (public_key, private_key)

def getEncryptedNumber(secret_number_list): # get encrypted number from paillier homomorphic algorithm
    encrypted_number_list = [public_key.encrypt(x).ciphertext() for x in secret_number_list]
    return encrypted_number_list

def getDecryptedNumber(encrypted_number_list, public_key, private_key): # get decrypted number from paillier homomorphic algorithm
    _encrypted_number_list = [paillier.EncryptedNumber(public_key, x, 0) for x in encrypted_number_list]
    decrypted_number_list = [private_key.decrypt(x) for x in _encrypted_number_list]
    return decrypted_number_list


if __name__=='__main__':
    secret_number_list = [55, 77, 36698] # change number you want to test here
    public_key, private_key = getKey()
    encrypted_number_list = getEncryptedNumber(secret_number_list) # the type of each item in encrypted_number_list is 'int'

    print(f'there are {len(encrypted_number_list)} numbers and their type is {type(encrypted_number_list[0])}')

    # Split each secret number
    shares_list = []
    combine_list = []
    for num in encrypted_number_list:
        shares_list.append(shamirs.shares(num, quantity=6, threshold=4, modulus=2**9689-1))
    print(f'The secret number is splitted into 6 shares with threshold 4')

    # Pick random chunks in each secret number
    pick_list = []
    for num in shares_list:
        pick_list.append(random.sample(num, 4))
    print(f'Partial shares are picked')

    # Combine chunks in each secret number
    combine_list = []
    for num in pick_list:
        combine_list.append(shamirs.interpolate(num))
    print(f'The shares are combined')

    # Decrypted
    decrypted_number_list = getDecryptedNumber(combine_list, public_key, private_key) # the type of each item in encrypted_number_list should be 'int'

    print(f'there are {len(decrypted_number_list)} numbers and the value is below:')
    for number in decrypted_number_list:
        print(number)