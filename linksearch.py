import requests
import re
from lxml import etree
import os
                 #while循环初始
link = input("你需要查找的网站")
url="http://"+link
url1=requests.get(url)              #get网址
url2=url1.text
html=etree.HTML(url2)
print("1 获得网页下全部的连接")
print("2 获得前缀不是www的连接")
print("3 获取all.txt下所有链接，并查询子链接")
linksearch = int(input("你需要得到的连接"))

def all():
    zac=html.xpath('//a/@href')
    str = '\n'
    f = open("all.txt", "w")
    f.write(str.join(zac))
    f.close()

def Prefix():
    zac = html.xpath('//a/@href')
    prefix=[]
    for i in zac:
        a = i[0:10]
        b = i[0]
        if a!="http://www" and b !="." and b!="#":
            prefix.append(i)
    str = '\n'
    f = open("pre.txt", "w")
    f.write(str.join(prefix))
    f.close()

def allofall(): #扫描页面下的连接，打开链接继续扫描 深度扫描
        filterlink = input("请输入网站主要字符,例如www.baidu.com，请输入baidu，这样可以大幅度筛选:")
        result = []
        with open("all.txt", encoding='utf-8') as f:
            for line in f:
                result.append(line.strip('\n').split(',')[0])  # 将每行字符串添加到列表result中
        num = 0  # 判断条件
        lenNum = len(result)  # 判断列表长度
        while True:
            website = result[num]
            try:
                website1 = requests.get(website)
            except BaseException:
                num += 1
                continue
            website2 = website1.text
            html = etree.HTML(website2)
            zac = html.xpath('//a/@href')
            filternum = 0
            filterlennum = len(zac)
            filternum1 = filterlennum
            filternum2 = []
            while True:
                if filterlink not in zac[filternum]:
                    filternum2.append(filternum)
                    filternum += 1
                    if filternum == filternum1:
                        break
                else:
                    filternum += 1
                    if filternum == filternum1:
                        break

            newzac = [v for i, v in enumerate(zac) if i not in filternum2]

            str = '\n'
            f = open("all1.txt", "a")
            f.write(str.join(newzac))
            f.close()

if linksearch==1:
    all()
elif linksearch==2:
    Prefix()
elif linksearch==3:
    all()
    allofall()
os.system("pause")


