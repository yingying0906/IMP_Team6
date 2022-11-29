import random
import lib
import shamirs

if __name__=='__main__':
    secret_number_list = [55, 77, 36698] # change number you want to test here
    public_key, private_key = lib.getKey()
    encrypted_number_list = lib.getEncryptedNumber(secret_number_list, public_key) # the type of each item in encrypted_number_list is 'int'

    print(f'there are {len(encrypted_number_list)} numbers and their type is {type(encrypted_number_list[0])}')

    # Split each secret number
    N, T = 10, 5 
    shares_list = []
    combine_list = []
    for i in encrypted_number_list:
        shares_list.append(shamirs.shares(i, quantity=N, threshold=T, modulus=lib.MODULUS))
    print(f'The secret number is splitted into %d shares with threshold %d' % (N, T)) 

    # Pick random chunks in each secret number
    pick_list = []
    for i in shares_list:
        pick_list.append(random.sample(i, T))
    print(f'Partial shares are picked')

    # Combine chunks in each secret number
    combine_list = []
    for i in pick_list:
        combine_list.append(shamirs.interpolate(i))
    print(f'The shares are combined')

    # Decrypted
    decrypted_number_list = lib.getDecryptedNumber(combine_list, public_key, private_key) # the type of each item in encrypted_number_list should be 'int'

    print(f'there are {len(decrypted_number_list)} numbers and the value is below:')
    for number in decrypted_number_list:
        print(number)