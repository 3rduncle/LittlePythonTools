#coding:utf8
import sys
import numpy as np

class Reservoid(object):
	def __init__(self, size):
		self.sie = size
		self.pool = []
	
	def add(self, item):
		if len(self.pool) < size:
			self.pool.append(line)
			return
		# randint(index) 从[0,index)中随机取值
		m = np.random.randint(index + 1)
		if (m < size):
			self.pool[m] = item
		return

if __name__ == '__main__':
	size = int(sys.argv[1])
	reservoid = Reservoid(size)
	for index, line in enumerate(sys.stdin):
		line = line.rstrip('\n')
		reservoid.add(line)
	for line in reservoid.pool:
		print line
