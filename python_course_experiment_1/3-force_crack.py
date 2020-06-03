import random
import string
import re
import zipfile

def random_key(L):
    '''
    生成随机密钥
    '''
    seq = string.ascii_letters + string.digits
    keylist = [random.choice(seq) for i in range(L)]
    return ''.join(keylist)

def random_digit(L):
    chars = string.digits  
    key_list = [random.choice(chars) for i in range(L)]
    return ''.join(key_list) 
# print(random_key(10)) 

def check_key(key):
    if len(key)<8:
        return False
    else:
        up_letter = re.search('[A-Z]',key)
        low_letter = re.search('[a-z]',key)
        digit = re.search('[0-9]',key)
        if up_letter != None and low_letter != None and digit != None:
            return True
        else:
            return False
# test_list = ['13t11jtk','12345678901','3aA245362','123t2lASDJ','password','Avbw23r9gfs','23523523613','AJFQWEFQWFK']
# print([(i,check_key(i)) for i in test_list])

def force_zip(zip_path,cipher):
    zip = zipfile.ZipFile(zip_path,'r')
    try:
        zip.extractall(pwd=str.encode(cipher))
        print("解压成功！密码为："+cipher)
        zip.close()
        return True
    except:
        # print("error！密码为："+cipher)
        return False


while(not(force_zip(r'target.zip',cipher=random_digit(5)))):
    cipher = random_digit(5)
