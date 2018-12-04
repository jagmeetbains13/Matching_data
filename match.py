#!/usr/bin/env python
# Author: Jagmeet Singh     [IISER Mohali]
# jagmeetbains13@gmail.com


f1 = open("data1.txt", "r")
f2 = open("data2.txt", "r")  
f3 = open("odata.txt", "w") 
i=0
while(1):
	i=i+1
	print i
	a = f1.readline()
	b = f2.readline()
	if not a:
		break
	c = a.split()
	d = b.split()
	while(1):
		i=i+1
		print i
		print c[0], c[1],d
		
		if(c[0][0] == d[0][0] and c[0][1] == d[0][1] and c[0][3] == d[0][3] and c[0][4] == d[0][4] and c[1] == d[1]):
			f3.write(c[0])
			f3.write(' ')
			f3.write(c[1])
			print c[0], c[1], d[1]
			f3.write(' ')
			for i in range(2,9):
				f3.write(c[i])
				f3.write(' ')
			f3.write(' ')
			for i in range(2,11):
			
				f3.write(d[i])
				f3.write(' ')
			f3.write('\n')
			break
		else:
			b =f2.readline()
			d = b.split()
		if not b:
			break
	
f1.close()
f2.close()
f3.close()		
		
	
 
