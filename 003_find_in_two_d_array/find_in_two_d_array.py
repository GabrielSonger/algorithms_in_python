import unittest

class Solution:
	def find_num_in_two_d_array(self, array, target):
		if not isinstance(array, list) or not isinstance(target, int):
			return False

		row = 0
		column = len(array[0]) - 1
		

		while row < len(array[0]) and column > 0:
			if array[row][column] == target:
				return True
			elif array[row][column] > target:
				column -= 1
			elif array[row][column] < target:
				row += 1

		return False

	def pythonic_way(self, array, target):
		result = next((True for sub_array in array if target in sub_array), False)
		
		return result

class Test(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.s = Solution()

	def test_target_in_array(self):
		array = [ 	[3, 5, 7],
				  	[11, 13, 19],
				 	[39, 45, 80],
				]
		self.assertTrue(self.s.find_num_in_two_d_array(array, 45))
		self.assertTrue(self.s.pythonic_way(array, 45))

	def test_target_not_in_array(self):
		array = [ 	[3, 5, 7],
				  	[11, 13, 19],
				 	[39, 45, 80],
				]

		self.assertFalse(self.s.find_num_in_two_d_array(array, 99))
		self.assertFalse(self.s.pythonic_way(array, 99))

if __name__ == '__main__':
	unittest.main()