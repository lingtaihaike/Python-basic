department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.12456
COURSE_FEES_Python = 1234.3456

line1 = 'Department1:name:%-15sManager:%-15sCOURSE_FEES:%-15.2fThe End!'%(department1,depart1_m,COURSE_FEES_SEC)
line2 = 'Department2:name:%-15sManager:%-15sCOURSE_FEES:%-15.2fThe End!'%(department2,depart2_m,COURSE_FEES_Python)

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)


line3 = f'Department1:name:{department1:<15}Manager:{depart1_m:<15}COURSE_FEES:{COURSE_FEES_SEC:<15.2f}The End!'
line4 = f'Department2:name:{department2:<15}Manager:{depart2_m:<15}COURSE_FEES:{COURSE_FEES_Python:<15.2f}The End!'
length = len(line3)
print('='*length)
print(line3)
print(line4)
print('='*length)

line5 = 'Department1:name:{:<15}Manager:{:<15}COURSE_FEES:{:<15.2f}The End!'.format(department1,depart1_m,COURSE_FEES_SEC)
line6 = 'Department2:name:{:<15}Manager:{:<15}COURSE_FEES:{:<15.2f}The End!'.format(department2,depart2_m,COURSE_FEES_Python)
length = len(line5)
print('='*length)
print(line5)
print(line6)
print('='*length)