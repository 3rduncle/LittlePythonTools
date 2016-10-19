#coding:utf8
import sys
import random

class Reservoid(object):
	def __init__(self, size):
		self.size = size
		self.pool = []
		self.index = 0
	
	def add(self, item):
		self.index += 1
		if len(self.pool) < self.size:
			self.pool.append(item)
			return
		# numpy.random.randint(index) 从[0,index)中随机取值
		# random.randint(0, index) 从[0,index]中随机取值
		m = random.randint(0, self.index - 1)
		if (m < self.size):
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
