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
print("1 获得网页下全部的连接（无过滤）")
print("2 获得前缀不是www的连接（有过滤）")
print("3 经过选项1的扫描之后，根据文件再次进行一轮扫描（无过滤）(时间长，慎选）")
print("4 获取前缀是http的连接（有过滤）")
linksearch = int(input("你需要得到的连接"))

def all():
    zac=html.xpath('//a/@href')
    str = '\n'
    f = open("all.txt", "w")
    f.write(str.join(zac))
    f.close()

def filter():
    zac = html.xpath('//a/@href')
    str = '\n'
    zac1 = []
    num = 0
    filter=[]
    for i in zac:
        zac1.append(i)
    for i in zac1:
        a = i[0:4]
        if a != "http":
            filter.append(num)
            num += 1
        else:
            num += 1
    newzac = [v for i, v in enumerate(zac1) if i not in filter]
    f = open("all.txt", "w")
    f.write(str.join(newzac))
    f.close()


def Prefix():
    zac = html.xpath('//a/@href')
    prefix=[]
    for i in zac:
        a = i[0:10]

        if a!="http://www":
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
elif linksearch==4:
    filter()
os.system("pause")


