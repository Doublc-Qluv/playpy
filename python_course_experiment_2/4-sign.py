from Crypto.PublicKey import RSA
from Crypto.Hash import MD5
from Crypto.Signature import pkcs1_15 

key = RSA.generate(2048)

def generateKey():
    '''
    准备一个私钥文件，一个公钥文件，一个数据文件
    '''
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    data = '''利用Python实现RSA数字签名的产生和验证过程。
  任务1：准备一个私钥文件，一个公钥文件，一个数据文件；
  任务2：定义一个函数，能够使用指定的私钥对数据文件进行签名，并将签名结果输出到文件返回；
  任务3：定义一个函数，能够使用指定的公钥对任务2中的签名文件进行验证，返回验证结果；
  任务4：利用任务1中的文件对任务2和3中的函数进行测试。'''
    with open("private_key.pem", "wb") as prifile,open("public_key.pem", "wb") as pubfile,open("data.txt","a") as datafile:
        prifile.write(private_key)
        pubfile.write(public_key)
        datafile.write(data)

# 读取data的内容
with open("data.txt","r") as datafile:
    data = datafile.read()

print(data)


def signAturer(private_key,data):
    '''
    签名函数，能够使用指定的私钥对数据文件进行签名，并将签名结果输出到文件返回
    '''
    # 获取消息的HASH值，摘要算法MD5，验证时也必须用MD5
    digest = MD5.new(data.encode('utf-8'))
    # 使用私钥对HASH值进行签名
    signature = pkcs1_15.new(private_key).sign(digest)
    # 将签名结果写入文件
    sig_results = open("sign_results.txt","wb")
    sig_results.write(signature)
    sig_results.close()
    return sig_results

def verifier(public_key,data,signature):
    '''
    签名验证函数，能够使用指定的公钥对任务2中的签名文件进行验证，返回验证结果
    '''
    digest = MD5.new(data.encode('utf-8'))
    try:
        pkcs1_15.new(public_key).verify(digest, signature)
        print("验证成功！！！")
    except:
        print("签名无效！！！")

def test():        
    '''
    利用任务1中的文件对任务2和3中的函数进行测试。
    '''
    with open('private_key.pem') as prifile,open('data.txt') as datafile:
        private_key = RSA.import_key(prifile.read())
        data = datafile.read()
        signAturer(private_key,data)

    with open('public_key.pem') as pubfile,open('data.txt') as datafile,open('sign_results.txt','rb') as sigfile:
        public_key = RSA.import_key(pubfile.read())
        data = datafile.read()
        signature = sigfile.read()
        verifier(public_key,data,signature)

if __name__ == "__main__":
    test()
