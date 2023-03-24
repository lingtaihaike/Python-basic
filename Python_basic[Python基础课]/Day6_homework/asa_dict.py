import re
asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO\nTCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"

asa_dict = {}
for conn in asa_conn.split('\n'):
    re.result = re.match('TCP Student (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d+) Teacher (\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}):(\d+), idle \d+:\d+:\d+, bytes (\d+), flags (UIO)',conn).groups()
    asa_dict[re.result[0],re.result[1],re.result[2],re.result[3]]=(re.result[4],re.result[5])
print('打印分析后的字典！\n')
print(asa_dict)

src = 'src'
src_ip = 'src_ip'
dst = 'dst'
dst_ip = 'dst_ip'
bytes_name = 'bytes'
flags = 'flags'
format_str1 = '{0:^10}: {1:^16}|{2:^10}:{3:^10}|{4:^8}:{5:^16}|{6:^10}:{7:^10}'
format_str2 = '{0:^10}: {1:^16}|{2:^10}:{3:^10}'
print('\n格式化打印输出\n')
for key,value in asa_dict.items():
    a,b,c,d = key
    e,f = value
    output1 = format_str1.format(src, a, src_ip, b,dst, c, dst_ip, d)
    output2 = format_str2.format(bytes_name, e, flags, f)
    print(output1)
    print(output2)
    print("="*len(output1))


