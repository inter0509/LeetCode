class Queue(object):
	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.stack = [];
	
	def push(self, x):
		"""
		:type x: int
		:rtype: nothing
		"""
		
		swap = [];
		while self.stack:
			top = self.stack.pop();
			swap.append(top);
		swap.append(x);
		while swap:
			self.stack.append(swap.pop());
	
	def pop(self):
		"""
		:rtype: nothing
		"""
		self.stack.pop();
	
	def peek(self):
		"""
		:rtype: int
		"""
		return self.stack[-1];
	
	def empty(self):
		"""
		:rtype: bool
		"""
		
		return (not self.stack);