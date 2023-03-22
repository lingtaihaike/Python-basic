import os
import re

ifconfig_result = os.popen('ifconfig ' + 'eth0').read()
# print(ifconfig_result)
#正则表达式查找ip,掩码，广播和mac地址
ipv4_add = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ifconfig_result)[0]
netmask = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ifconfig_result)[1]
broadcast = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ifconfig_result)[2]
mac_addr = re.findall('[0-9a-f]{1,2}:[0-9a-f]{1,2}:[0-9a-f]{1,2}:[0-9a-f]{1,2}:[0-9a-f]{1,2}:[0-9a-f]{1,2}',ifconfig_result)[0]
# print(ipv4_add,netmask,broadcast,mac_addr)
# 格式化字符串
string_format = '{0:<15}: {1}'
# 打印结果
print(string_format.format(r'ipv4_add',ipv4_add))
print(string_format.format(r'netmask',netmask))
print(string_format.format(r'broadcast',broadcast))
print(string_format.format(r'mac_addr',mac_addr))

#产生网关地址
ip_r = os.popen('ip '+'r').read()
ipv4_gw = re.findall('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',ip_r)[0]
print('\n我们假设网关IP地址为第一位1，因此网关地址为:' + ipv4_gw+ '\n')

#ping网关
ping_result = os.popen('ping ' + ipv4_gw + ' -c 1').read()
# print(ping_result)
re_ping_result = re.findall('icmp_seq=1',ping_result)
if re_ping_result:
    print('网关可达！')
else:
    print('网关不可达！')



