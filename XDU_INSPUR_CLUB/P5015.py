# 标题中可能包含大、小写英文字母、数字字符、空格和换行符。统计标题字 符数时，空格和换行符不计算在内
a = str(input())
a = a.replace(" ","").replace('\n', '').replace('\r', '')
lens = len(a)
print(lens)