
class Solution:

	def recursive_fibonacci(self, num):
		if num < 0 or not isinstance(num, int):
			return
		elif num == 0 or num == 1:
			return num
		else:
			return self.regular_fibonacci(n - 1) + self.regular_fibonacci(n - 2)

	def iterative_fibonacci(self, num):
		if num < 0 or not isinstance(num, int):
			return
		
		f_first = 0
		f_second = 1
		f_sum = 0

		for i in range(num - 1):
			f_sum = f_first + f_second
			f_first = f_second
			f_second = f_sum

		return f_sum

