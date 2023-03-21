import re

str = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'

re_result = re.match('(\d{1,4})\s+([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})\s+(\S+)\s+(\S+)',str).groups()
print('%-15s: %s'%('VLAN ID',re_result[0]))
print('%-15s: %s'%('MAC',re_result[1]))
print('%-15s: %s'%('TYPE',re_result[2]))
print('%-15s: %s'%('Interface',re_result[3]))




