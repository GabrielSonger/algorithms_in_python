
class StackWithTwoQueue:
	def __init__(self):
		self.queue1 = []
		self.queue2 = []

	def push(self, element):
		if not element:
			return 

		if self.queue1:
			self.queue1.append(element)
		else:
			self.queue2.append(element)

	def pop(self):
		if not self.queue1 and not self.queue2:
			return None

		if self.queue1:
			while len(self.queue1) > 1:
				self.queue2.append(self.queue1.pop(0))

			return self.queue1.pop()
		else:
			while len(self.queue2) > 1:
				self.queue1.append(self.queue2.pop(0))
			
			return self.queue2.pop()

s = StackWithTwoQueue()
s.push(1)
s.push(2)
s.push(3)
print (s.pop())
print (s.pop())
print (s.pop())