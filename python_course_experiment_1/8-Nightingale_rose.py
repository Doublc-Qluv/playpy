import matplotlib.pyplot as plt
import numpy as np
import xlrd

#####按列读取excel文件并存入两个列表#####
data=xlrd.open_workbook(r'data.xlsx') 
table  = data.sheets()[0]   #通过索引顺序获取工作表
cols_n = table.ncols 
country_list = table.col_values(0,start_rowx=1) # start_rowx默认为0，设置为1去掉列名
data_list = table.col_values(1,start_rowx=1)
#####计算角度#####
n = table.nrows-1           #去掉列名
theta = np.linspace(0,2*np.pi,len(data_list))    # 360度等分成n份

#####作图#####
# 设置画布
fig = plt.figure(figsize=(18,15))
# 极坐标
ax = plt.subplot(111,projection = 'polar')
# 顺时针并设置N方向为0度
ax.set_theta_direction(1)
ax.set_theta_zero_location('N') 

# 在极坐标中画柱形图
ax.bar(theta,
        data_list,
        width = 0.33,
        color = np.random.random((len(data_list),3)),
        align = 'edge')

#####显示一些简单的中文图例#####

plt.rcParams ['font.family'] = ['sans-serif']
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
ax.set_title('大陆省市面积top20',fontdict={'fontsize':10})
for angle,data,country in zip(theta,data_list,country_list):
    ax.text(angle+0.05,data+100,str(country)) 
plt.axis('off')
plt.savefig('Nightingale_rose.png')
plt.show()