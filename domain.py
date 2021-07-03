import os
import sys
#涉及敏感操作，需要用管理员权限启动该程序

iplist = list()
ip = str(input("请输入你的网段，例如192.168.0 或者192.168.50"))
ip1 = ip
for i in range(0,255):
    ip1 = ip
    a = str(i)
    ip1=ip1+'.'+a
    backinfo = os.system('ping -c 1 -w 1 %s' % ip1)  # 实现pingIP地址的功能，-c1指发送报文一次，-w指等待n秒
    if backinfo:
        pass
    else:
        iplist.append(ip1)
print(iplist)
