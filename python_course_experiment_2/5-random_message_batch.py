import random
import string
# 百家姓
name = '赵 钱 孙 李 周 吴 郑 王 冯 陈 褚 卫 蒋 沈 韩 杨 朱 秦 尤 许 何 吕 施 张 孔 曹 严 华 金 魏 陶 姜 戚 谢 邹 喻 柏 水 窦 章'\
'云 苏 潘 葛 奚 范 彭 郎 鲁 韦 昌 马 苗 凤 花 方 俞 任 袁 柳 酆 鲍 史 唐 费 廉 岑 薛 雷 贺 倪 汤 滕 殷 罗 毕 郝 邬 安 常'\
'乐 于 时 傅 皮 卞 齐 康 伍 余 元 卜 顾 孟 平 黄 和 穆 萧 尹 姚 邵 湛 汪 祁 毛 禹 狄 米 贝 明 臧 计 伏 成 戴 谈 宋 茅 庞'\
'熊 纪 舒 屈 项 祝 董 梁 杜 阮 蓝 闵 席 季 麻 强 贾 路 娄 危 江 童 颜 郭 梅 盛 林 刁 钟 徐 邱 骆 高 夏 蔡 田 樊 胡 凌 霍'\
'虞 万 支 柯 昝 管 卢 莫 经 房 裘 缪 干 解 应 宗 丁 宣 贲 邓 郁 单 杭 洪 包 诸 左 石 崔 吉 钮 龚 程 嵇 邢 滑 裴 陆 荣 翁'\
'荀 羊 於 惠 甄 曲 家 封 芮 羿 储 靳 汲 邴 糜 松 井 段 富 巫 乌 焦 巴 弓 牧 隗 山 谷 车 侯 宓 蓬 全 郗 班 仰 秋 仲 伊 宫'\
'宁 仇 栾 暴 甘 钭 厉 戎 祖 武 符 刘 景 詹 束 龙 叶 幸 司 韶 郜 黎 蓟 薄 印 宿 白 怀 蒲 邰 从 鄂 索 咸 籍 赖 卓 蔺 屠 蒙'\
'池 乔 阴 鬱 胥 能 苍 双 闻 莘 党 翟 谭 贡 劳 逄 姬 申 扶 堵 冉 宰 郦 雍 卻 璩 桑 桂 濮 牛 寿 通 边 扈 燕 冀 郏 浦 尚 农'\
'温 别 庄 晏 柴 瞿 阎 充 慕 连 茹 习 宦 艾 鱼 容 向 古 易 慎 戈 廖 庾 终 暨 居 衡 步 都 耿 满 弘 匡 国 文 寇 广 禄 阙 东'\
'欧 殳 沃 利 蔚 越 夔 隆 师 巩 厍 聂 晁 勾 敖 融 冷 訾 辛 阚 那 简 饶 空 曾 毋 沙 乜 养 鞠 须 丰 巢 关 蒯 相 查 后 荆 红'\
'游 竺 权 逯 盖 益 桓 公 万俟 司马 上官 欧阳 夏侯 诸葛 闻人 东方 赫连 皇甫 尉迟 公羊 澹台 公冶 宗政 濮阳 淳于 单于 太叔 申屠'\
'公孙 仲孙 轩辕 令狐 钟离 宇文 长孙 慕容 鲜于 闾丘 司徒 司空 丌官 司寇 仉督 子车 颛孙 端木 巫马 公西 漆雕 乐正 壤驷 公良 拓跋'\
'夹谷 宰父 谷梁 晋楚 闫法 汝鄢 涂钦 段干 百里 东郭 南门 呼延 归海 羊舌 微生 岳帅 缑亢 况郈 有琴 梁丘 左丘 东门 西门 商牟 佘佴'\
'伯赏 南宫 墨哈 谯笪 年爱 阳佟 第五 言福'
name1 = name.split(" ")
# print(name1)

#常见的字
name2="\u7684\u4e00\u662f\u4e86\u6211\u4e0d\u4eba\u5728\u4ed6\u6709\u8fd9\u4e2a\u4e0a\u4eec\u6765"\
      "\u5230\u65f6\u5927\u5730\u4e3a\u5b50\u4e2d\u4f60\u8bf4\u751f\u56fd\u5e74\u7740\u5c31\u90a3"\
"\u548c\u8981\u5979\u51fa\u4e5f\u5f97\u91cc\u540e\u81ea\u4ee5\u4f1a\u5bb6\u53ef\u4e0b\u800c"\
"\u8fc7\u5929\u53bb\u80fd\u5bf9\u5c0f\u591a\u7136\u4e8e\u5fc3\u5b66\u4e48\u4e4b\u90fd\u597d"\
"\u770b\u8d77\u53d1\u5f53\u6ca1\u6210\u53ea\u5982\u4e8b\u628a\u8fd8\u7528\u7b2c\u6837\u9053"\
"\u60f3\u4f5c\u79cd\u5f00\u7f8e\u603b\u4ece\u65e0\u60c5\u5df1\u9762\u6700\u5973\u4f46\u73b0"\
"\u524d\u4e9b\u6240\u540c\u65e5\u624b\u53c8\u884c\u610f\u52a8\u65b9\u671f\u5b83\u5934\u7ecf"\
"\u957f\u513f\u56de\u4f4d\u5206\u7231\u8001\u56e0\u5f88\u7ed9\u540d\u6cd5\u95f4\u65af\u77e5"\
"\u4e16\u4ec0\u4e24\u6b21\u4f7f\u8eab\u8005\u88ab\u9ad8\u5df2\u4eb2\u5176\u8fdb\u6b64\u8bdd"\
"\u5e38\u4e0e\u6d3b\u6b63\u611f\u89c1\u660e\u95ee\u529b\u7406\u5c14\u70b9\u6587\u51e0\u5b9a"\
"\u672c\u516c\u7279\u505a\u5916\u5b69\u76f8\u897f\u679c\u8d70\u5c06\u6708\u5341\u5b9e\u5411"\
"\u58f0\u8f66\u5168\u4fe1\u91cd\u4e09\u673a\u5de5\u7269\u6c14\u6bcf\u5e76\u522b\u771f\u6253"\
"\u592a\u65b0\u6bd4\u624d\u4fbf\u592b\u518d\u4e66\u90e8\u6c34\u50cf\u773c\u7b49\u4f53\u5374"\
"\u52a0\u7535\u4e3b\u754c\u95e8\u5229\u6d77\u53d7\u542c\u8868\u5fb7\u5c11\u514b\u4ee3\u5458"\
"\u8bb8\u7a1c\u5148\u53e3\u7531\u6b7b\u5b89\u5199\u6027\u9a6c\u5149\u767d\u6216\u4f4f\u96be"\
"\u671b\u6559\u547d\u82b1\u7ed3\u4e50\u8272\u66f4\u62c9\u4e1c\u795e\u8bb0\u5904\u8ba9\u6bcd"\
"\u7236\u5e94\u76f4\u5b57\u573a\u5e73\u62a5\u53cb\u5173\u653e\u81f3\u5f20\u8ba4\u63a5\u544a"\
"\u5165\u7b11\u5185\u82f1\u519b\u5019\u6c11\u5c81\u5f80\u4f55\u5ea6\u5c71\u89c9\u8def\u5e26"\
"\u4e07\u7537\u8fb9\u98ce\u89e3\u53eb\u4efb\u91d1\u5feb\u539f\u5403\u5988\u53d8\u901a\u5e08"\
"\u7acb\u8c61\u6570\u56db\u5931\u6ee1\u6218\u8fdc\u683c\u58eb\u97f3\u8f7b\u76ee\u6761\u5462"\
"\u75c5\u59cb\u8fbe\u6df1\u5b8c\u4eca\u63d0\u6c42\u6e05\u738b\u5316\u7a7a\u4e1a\u601d\u5207"\
"\u600e\u975e\u627e\u7247\u7f57\u94b1\u7d36\u5417\u8bed\u5143\u559c\u66fe\u79bb\u98de\u79d1"\
"\u8a00\u5e72\u6d41\u6b22\u7ea6\u5404\u5373\u6307\u5408\u53cd\u9898\u5fc5\u8be5\u8bba\u4ea4"\
"\u7ec8\u6797\u8bf7\u533b\u665a\u5236\u7403\u51b3\u7aa2\u4f20\u753b\u4fdd\u8bfb\u8fd0\u53ca"\
"\u5219\u623f\u65e9\u9662\u91cf\u82e6\u706b\u5e03\u54c1\u8fd1\u5750\u4ea7\u7b54\u661f\u7cbe"\
"\u89c6\u4e94\u8fde\u53f8\u5df4\u5947\u7ba1\u7c7b\u672a\u670b\u4e14\u5a5a\u53f0\u591c\u9752"\
"\u5317\u961f\u4e45\u4e4e\u8d8a\u89c2\u843d\u5c3d\u5f62\u5f71\u7ea2\u7238\u767e\u4ee4\u5468"\
"\u5427\u8bc6\u6b65\u5e0c\u4e9a\u672f\u7559\u5e02\u534a\u70ed\u9001\u5174\u9020\u8c08\u5bb9"\
"\u6781\u968f\u6f14\u6536\u9996\u6839\u8bb2\u6574\u5f0f\u53d6\u7167\u529e\u5f3a\u77f3\u53e4"\
"\u534e\u8ae3\u62ff\u8ba1\u60a8\u88c5\u4f3c\u8db3\u53cc\u59bb\u5c3c\u8f6c\u8bc9\u7c73\u79f0"\
"\u4e3d\u5ba2\u5357\u9886\u8282\u8863\u7ad9\u9ed1\u523b\u7edf\u65ad\u798f\u57ce\u6545\u5386"\
"\u60ca\u8138\u9009\u5305\u7d27\u4e89\u53e6\u5efa\u7ef4\u7edd\u6811\u7cfb\u4f24\u793a\u613f"\
"\u6301\u5343\u53f2\u8c01\u51c6\u8054\u5987\u7eaa\u57fa\u4e70\u5fd7\u9759\u963f\u8bd7\u72ec"\
"\u590d\u75db\u6d88\u793e\u7b97\u4e49\u7adf\u786e\u9152\u9700\u5355\u6cbb\u5361\u5e78\u5170"\
"\u5ff5\u4e3e\u4ec5\u949f\u6015\u5171\u6bdb\u53e5\u606f\u529f\u5b98\u5f85\u7a76\u8ddf\u7a7f"



#姓名
def getName():
    '''
    随机生成姓名
    '''
    name=random.choice(name1)
    for i in range(random.choice([2,3,4])-1):
        name=name+random.choice(name2)
    return name

#地址
def getAddress():
      address = ''
      for i in range(random.choice(list(range(10,31)))):
            address=address+random.choice(name2)
      return address

#性别
def sex():
      return random.choice(["男","女"])

#
def phoneNumber():
    '''
    电话号码，手机号码是一个字符串，11位
    '''
    number="1"#假设电话开头数字是1
    for i in range(10):#剩下的10位
        number=number+random.choice(string.digits)#string.digits 返回'0123456789'
    return number

#年龄
def age():
      return str(random.randint(18,100))

#邮箱
def Email():
    email=''
    domain = ['163','189','qq','hotmail','gmail','sohu','sina']
    suffix = ['com', 'org', 'net', 'cn', 'abc', 'club']
    for i in range(random.randint(6,12)):
        email=email+random.choice(string.ascii_letters+string.digits)
    email=email+'@'+random.choice(domain)+'.'+random.choice(suffix)
    return email

def main(n):
    '''
    将信息输入到文本之中去
    '''
    f=open("information.txt","w")
    head = '姓名'+'   '+'性别'+'   '+'年龄'+'   '+'电话号码'+'   '+'电子邮箱'+'\n'# 设置表头
    f.writelines(head) 
    for i in range(n):
        message=list(getName()+"   "+sex()+"   "+age()+"   "+phoneNumber()+'   '+Email()   )
        f.writelines(message)   
        f.writelines("\n")      
    f.close()


def read():
    '''
    读取文本中的信息
    '''
    f=open("information.txt","r")
    for line in f:                
        print(line)
    f.close()
# n=int(input("你需要随机生成多少条数据："))
n=4
# main(n)
print([Email() for i in range(5)])