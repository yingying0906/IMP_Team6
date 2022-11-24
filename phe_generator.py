# Download the pyphe package 
# using pip: 
# $ pip install phe

from phe import paillier

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
    secret_number_list = [1, 2, 3] # change number you want to test here
    public_key, private_key = getKey()
    encrypted_number_list = getEncryptedNumber(secret_number_list) # the type of each item in encrypted_number_list is 'int'

    print(f'there are {len(encrypted_number_list)} numbers and their type is {type(encrypted_number_list[0])}')

    # Do data splitting here

    decrypted_number_list = getDecryptedNumber(encrypted_number_list, public_key, private_key) # the type of each item in encrypted_number_list should be 'int'

    print(f'there are {len(decrypted_number_list)} numbers and the value is below:')
    for number in decrypted_number_list:
        print(number)