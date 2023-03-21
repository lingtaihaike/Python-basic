import re
show_conn = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'
test = r', | '
split_list = re.split(test,show_conn)
time_split = re.split(r':',split_list[6])
time1 = time_split[0] + '小时' + time_split[1] + '分钟' + time_split[2] + '秒'
print('%-20s: %s'%('protocol',split_list[0]))
print('%-20s: %s'%(split_list[1],split_list[2]))
print('%-20s: %s'%(split_list[3],split_list[4]))
print('%-20s: %s'%(split_list[5],time1))
print('%-20s: %s'%(split_list[7],split_list[8]))
print('%-20s: %s'%(split_list[9],split_list[10]))
