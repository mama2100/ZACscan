from lxml import etree
import os
import requests, argparse, sys, re
from requests.packages import urllib3
from urllib.parse import urlparse
from bs4 import BeautifulSoup

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
print("5 从JS中提取连接")
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
def JSZac():

    url = str(input("请输入您查询的网站，格式为http://www.baidu.com"))  # 你需要查询的网站
    urllib3.disable_warnings()  # 证书查询

    def extract_URL(JS):  # 正则表达式
        pattern_raw = r"""(?:"|')(((?:[a-zA-Z]{1,10}://|//)[^"'/]{1,}\.[a-zA-Z]{2,}[^"']{0,})|((?:/|\.\./|\./)[^"'><,;| *()(%%$^/\\\[\]][^"'><,;|()]{1,})|([a-zA-Z0-9_\-/]{1,}/[a-zA-Z0-9_\-/]{1,}\.(?:[a-zA-Z]{1,4}|action)(?:[\?|/][^"|']{0,}|))|([a-zA-Z0-9_\-]{1,}\.(?:php|asp|aspx|jsp|json|action|html|js|txt|xml)(?:\?[^"|']{0,}|)))(?:"|')"""
        pattern = re.compile(pattern_raw, re.VERBOSE)
        result = re.finditer(pattern, str(JS))
        if result == None:
            return None
        js_url = []
        return [match.group().strip('"').strip("'") for match in result if match.group() not in js_url]

    def process_url(URL, re_URL):
        black_url = ["javascript:"]
        URL_raw = urlparse(URL)  # 解析url
        host_URL = URL_raw.scheme
        if re_URL[0:2] == "//":
            result = host_URL + ":" + re_URL
        elif re_URL[0:4] == "http":
            result = re_URL
        else:
            result = URL
        return result

    def Extract_html(URL):
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"}
        try:
            raw = requests.get(URL, headers=header, timeout=3, verify=False)
            raw = raw.content.decode("utf-8", "ignore")
            return raw
        except:
            return None

    def jsurl(js=False):
        if js == False:
            try:
                print("url:" + url)
            except:
                print("请输入完整的连接，例如:https://www.baidu.com")
            html_raw = Extract_html(url)
            html = BeautifulSoup(html_raw, "html.parser")
            html_scripts = html.findAll("script")
            script_array = {}
            script_temp = ""
            for html_script in html_scripts:
                script_src = html_script.get("src")
                if script_src == None:
                    script_temp += html_script.get_text() + "\n"
                else:
                    purl = process_url(url, script_src)
                    script_array[purl] = Extract_html(purl)
            script_array[url] = script_temp
            allurls = []
            for script in script_array:
                # print(script)
                temp_urls = extract_URL(script_array[script])
                if len(temp_urls) == 0: continue
                for temp_url in temp_urls:
                    allurls.append(process_url(script, temp_url))

        txt = str(input("请输入文件保存的绝对路径"))
        with open(txt, 'a+', encoding='utf-8') as f:
            for data in allurls:
                f.write(data + '\n')
            f.close()

    jsurl()


if linksearch==1:
    all()
elif linksearch==2:
    Prefix()
elif linksearch==3:
    all()
    allofall()
elif linksearch==4:
    filter()
elif linksearch==5:
    JSZac()
os.system("pause")


