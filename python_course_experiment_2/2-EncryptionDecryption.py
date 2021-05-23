import secrets
import json
from pathlib import Path

def random_key(L):
    '''
    生成随机密钥，返回整数
    '''
    bytes_key = secrets.token_bytes(nbytes=L)
    int_key = int.from_bytes(bytes_key, byteorder='big') # 大端存储
    # int_key = int.from_bytes(bytes_key, byteorder='little') # 小端存储
    return int_key
# print(random_key(10))
def Encryption(string):
    '''
    将字符串参数编码为字节串并转换为整数，与一个随机密钥进行异或运算生成
    '''
    string_bytes = str.encode(string)
    int_string = int.from_bytes(string_bytes, byteorder='big')
    random_k = random_key(len(string_bytes))
    secret = int_string ^ random_k
    return {'key':random_k, 'secret':secret}

# random_k,secret = Encryption('abc')

def Decryption(random_k,secret):
    '''
    将密文和密钥异或，计算密文长度，返回字符串
    '''
    int_message = secret ^ random_k
    byte_message = int_message.to_bytes((int_message.bit_length() + 7) // 8,byteorder='big')
    str_message = bytes.decode(byte_message)
    return str(str_message)

string1 = "路漫漫其修远兮，吾将上下而求索。"
string2 = "Never put off until tomorrow what may be done today."

# # 选择要加解密的字符串
stringx = string1
print(Encryption(stringx))
Encryption_pair = Encryption(stringx)
print(Decryption(Encryption_pair['key'],Encryption_pair['secret']))

stringx = string2
print(Encryption(stringx))
Encryption_pair = Encryption(stringx)
print(Decryption(Encryption_pair['key'],Encryption_pair['secret']))

# path = 'key.txt'
def Encryption_file(path='key.txt'):
    '''
    加密文件，得到key和密文
    '''
    path = Path(path) # path of random_key
    message_path = 'message.txt'
    secret_path_new = 'secret_new.txt'

    with open(path,'wt',encoding='utf-8') as fkey, open(message_path,'rt',encoding='utf-8') as fmessage, open(secret_path_new,'wt',encoding='utf-8') as fsecret:
        Encryptiontxt = Encryption(fmessage.read())
        secret1, key1 = Encryptiontxt['secret'], Encryptiontxt['key']
        # print(Encryptiontxt)
        json.dump(key1,fkey)
        json.dump(secret1,fsecret)

def Decryption_file():
    '''
    解密文件，得到明文
    '''
    key_path = 'key.txt'
    message_path_new = 'message_new.txt'
    secret_path = 'secret_new.txt'

    with open(key_path,'rt',encoding='utf-8') as fkey, open(message_path_new,'wt',encoding='utf-8') as fmessage, open(secret_path,'rt',encoding='utf-8') as fsecret:
        Decryptiontxt = Decryption(json.load(fkey),json.load(fsecret))
        fmessage.write(Decryptiontxt)

# Encryption_file()
# Decryption_file()
