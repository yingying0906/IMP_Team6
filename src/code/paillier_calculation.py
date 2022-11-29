from phe import paillier

# 準備實際會送過來的資料
# (1)（type = list of ciphertext , index[0]=GOT , index[1]=GPT )
# (2) public_key

#keyring = paillier.PaillierPrivateKeyring()
#public_key, private_key = paillier.generate_paillier_keypair(keyring)
#GOT=30
#GPT=1003
#encrypted_GOT = public_key.encrypt(GOT) 
#encrypted_GPT = public_key.encrypt(GPT) 
#
#encrypted_number_list= [ paillier.EncryptedNumber.ciphertext(encrypted_GOT),paillier.EncryptedNumber.ciphertext(encrypted_GPT)]


################################################################################################################################################


#運算

def GOT_GPT_calc(encrypted_number_list,public_key):

    # 從 ciphertext 的 input 取得相對的 Encrypted Number Type 
    _encrypted_number_list = [paillier.EncryptedNumber(public_key, x, 0) for x in encrypted_number_list]
    GOT = _encrypted_number_list[0]
    GPT = _encrypted_number_list[1]
    neg_GOT = GOT.__mul__(-1)
    neg_GPT = GPT.__mul__(-1)

    # (1) calculation : GOT - GPT 
    neg_GPT_difference = GOT.__add__(neg_GPT)

    # (2) calculation : GOT - 40 , calculation : 200 - GOT  , relationship : and 
    GOT_difference_with_normal = GOT.__add__(-40)
    GOT_difference_with_upper = neg_GOT.__add__(200)

    # (3) calculation : GPT - GOT 
    neg_GOT_difference = GPT.__add__(neg_GOT)

    # (4.1) calculation : GPT - 40 , calculation : 200 - GPT , relationship : and 
    GPT_difference_with_normal = GPT.__add__(-40)
    GPT_difference_with_upper = neg_GPT.__add__(200)

    # (5) calculation : GOT - 1000 
    GOT_exceed = GOT.__add__(-1000)

    # (6) calculation : GPT - 1000 
    GPT_exceed = GPT.__add__(-1000)

    # 檢驗結果（result_value) = [ GOT大於GPT / GOT - GPT , GOT大於正常值 / GOT - 40 , GOT小於200(U/L) / 200 - GOT , GPT大於GOT / GPT - GOT, 
    #                             GPT大於正常值 / GPT - 40 , GPT小於200(U/L) / 200 - GPT , GOT大於1000(U/L) / GOT - 1000 , 或GPT大於1000(U/L) / GPT - 1000 ]
    # +ve : TRUE , -ve / 0 : FALSE 
    result_value = [ neg_GPT_difference , GOT_difference_with_normal , GOT_difference_with_upper , neg_GOT_difference ,  
                    GPT_difference_with_normal , GPT_difference_with_upper , GOT_exceed , GPT_exceed ]

    return result_value


#referenced table about GOT and GPT : https://media.discordapp.net/attachments/1039538722707865661/1047118328340152411/2022-11-22_8.27.16.png )
################################################################################################################################################


#檢查結果

#encrypted_result = GOT_GPT_calc(encrypted_number_list,public_key)
#decrypted_result = [private_key.decrypt(x) for x in encrypted_result]
#print("[ correct answer ]")
#print(decrypted_result)






