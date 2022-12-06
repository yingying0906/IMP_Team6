from phe import paillier

def getKey(): # get public key and private key from pyphe package
    public_key, private_key = paillier.generate_paillier_keypair()
    keyring = paillier.PaillierPrivateKeyring()
    keyring.add(private_key)
    return (public_key, private_key)

def getEncryptedNumber(secret_number_list, public_key): # get encrypted number from paillier homomorphic algorithm
    encrypted_number_list = [public_key.encrypt(x).ciphertext() for x in secret_number_list]
    return encrypted_number_list

def getDecryptedNumber(encrypted_number_list, public_key, private_key): # get decrypted number from paillier homomorphic algorithm
    _encrypted_number_list = [paillier.EncryptedNumber(public_key, x, 0) for x in encrypted_number_list]
    decrypted_number_list = [private_key.decrypt(x) for x in _encrypted_number_list]
    return decrypted_number_list

MODULUS = (2**9689)-1 # prime