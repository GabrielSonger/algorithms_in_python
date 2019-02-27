import unittest

class Solution:
	def replace_space_in_string(self, str_in):
		if not str_in or not isinstance(str_in, str):
			return None

		num_spaces = 0

		for character in str_in:
			if character == ' ':
				num_spaces += 1

		new_str_len = len(str_in) + 2 * num_spaces
		# Create new list with new string length
		new_str = [None] * new_str_len
		new_str_pointer, old_str_pointer = new_str_len - 1, len(str_in) - 1

		# python support negative index, so use 0 as condition
		while new_str_pointer >= old_str_pointer >= 0:
			if str_in[old_str_pointer] == ' ':
				new_str[new_str_pointer - 2 : new_str_pointer + 1] = ['%', '2', '0']
				new_str_pointer -= 3
				old_str_pointer -= 1
			else:
				new_str[new_str_pointer] = str_in[old_str_pointer]
				new_str_pointer -= 1
				old_str_pointer -= 1

		return ''.join(new_str)

	def pythonic_way(self, str_in):
		if not str_in or not isinstance(str_in, str):
			return None

		return str_in.replace(' ', '%20') 


class Test(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.s = Solution()

	def test_str_with_spaces(self):
		test_str = 'Hello World'
		output_str = 'Hello%20World'

		self.assertEqual(self.s.replace_space_in_string(test_str), output_str)
		self.assertEqual(self.s.pythonic_way(test_str), output_str)

	def test_str_without_space(self):
		test_str = 'Hello'

		self.assertEqual(self.s.replace_space_in_string(test_str), test_str)
		self.assertEqual(self.s.pythonic_way(test_str), test_str)


if __name__ == '__main__':
	unittest.main()