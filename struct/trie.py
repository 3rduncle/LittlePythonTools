import sys

class Node(object):
	def __init__(self, key, meta = None):
		self.key = key
		self.meta = meta
		self.parent = None
		self.children = {}

	def add_child(self, node):
		key = node.key
		hold = self.children.get(key)
		if hold is None:
			 hold = self.children.setdefault(key, node)
			 hold.parent = self
		else:
			assert hold.key == node.key
			assert hold.meta is None
			hold.meta = node.meta
			hold.merge(node)
		return self

	def merge(self, other):
		assert self.key == other.key
		for key, node in other.children.items():
			self.add_child(node)

	def has_meta(self):
		return not self.meta is None

	def set_meta(self, meta):
		self.meta = meta

	def path(self):
		if self.key == 'root':
			return ''
		elif self.parent is None:
			return self.key
		else:
			return self.parent.path() + self.key

	def top(self, k):
		if not self.children:
			assert self.meta
			return [self]
		candidate = []
		for child in self.children.values():
			candidate += child.top(k)
		sorted(candidate, key=lambda x:x.meta, reverse=True)
		return candidate[0:k]
	
class Trie(object):
	def __init__(self):
		self.root = Node("root")
		self.leaves = {}

	def insert(self, path, meta):
		nodes = map(Node, path[::-1])
		nodes[0].set_meta(meta)
		self.leaves[path] = nodes[0]
		for child, parent in zip(nodes, nodes[1:]):
			parent.add_child(child)
		self.root.add_child(nodes[-1])

	def search(self, path):
		cursor = self.root
		for key in path:
			cursor = cursor.children.get(key)
			if cursor is None: return cursor


def top(k):
	K = 10
	trie = Trie()
	for line in sys.stdin:
		line = line.rstrip('\n')
		path, meta = line.split('\t')
		path = path.decode('utf8')
		meta = int(meta)
		trie.insert(path, meta)

	buffer = {}
	for path, node in trie.leaves.items():
		candidate = node.parent.top(K)
		for leaf in candidate:
			path = leaf.path()
			if path not in buffer:
				buffer[path] = leaf

	for path, node in buffer.items():
		print "%s\t%d" % (path.encode('utf8'), node.meta)

def suggestion(k):
	trie = Trie()
	for line in open(sys.argv[1]):
		line = line.rstrip('\n')
		path, meta = line.split('\t')
		path = path.decode('utf8')
		meta = int(meta)
		trie.insert(path, meta)

	for line in sys.stdin:
		line = line.rstrip('\n')
		node = trie.search(line)
		if node is None:
			print '%s\tNone' % line
			continue
		for node in node.top(k):
			print '%s\t%s\t%d' % (line, node.path(), node.meta)

if __name__ == '__main__':
	suggestion(10)
	
