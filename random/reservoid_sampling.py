#coding:utf8
import sys
import numpy as np

size = int(sys.argv[1])
pool = []
for index, line in enumerate(sys.stdin):
	line = line.rstrip('\n')
	if index < size:
		pool.append(line)
	else:
		# randint(index) 从[0,index)中随机取值
		m = np.random.randint(index + 1)
		if (m < size):
			pool[m] = line

for line in pool:
	print line
