import re
str1 = 'Port-channel1.189      192.168.189.254    YES     CONFIG    up'

re_result = re.match('^([A-Z]\S+\d)\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+YES     CONFIG\s+(\w+)$', str1).groups()

if_name = re_result[0]
if_add = re_result[1]
if_status = re_result[2]

name = '接口'
add = 'IP地址'
status = '状态'

print(f'{name:<7}: {if_name:<}')
print(f'{add:<7}: {if_add}')
print(f'{status:<7}: {if_status}')

