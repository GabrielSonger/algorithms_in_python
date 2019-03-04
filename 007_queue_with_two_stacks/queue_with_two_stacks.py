
class QueueWithTwoStacks:
	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def push(self, element):
		self.stack1.append(element)

	def pop(self):
		if not self.stack1 and not self.stack2:
			return None

		if not self.stack2:
			while self.stack1:
				self.stack2.append(self.stack1.pop())

		return self.stack2.pop()


q = QueueWithTwoStacks()
q.push(1)
q.push(2)
q.push(3)
print (q.pop())
print (q.pop())
print (q.pop())

	

