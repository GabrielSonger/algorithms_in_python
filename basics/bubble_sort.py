import unittest

class BubbleSort:
	def bubble_sort(self, nums):
		if not nums:
			return 

		# when i = len(nums) - 1, last element is guranteed sorted
		for i in range(len(nums) - 1):
			for j in range(0, len(nums) - i - 1):
				if nums[j] > nums[j+1]:
					nums[j], nums[j+1] = nums[j+1], nums[j]

		return nums


class Test(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.b = BubbleSort()

	def test_regular_elements(self):
		nums = [10, 9, 8, 7, 11, 1]
		sorted_nums = [1, 7, 8, 9, 10, 11]

		self.assertEqual(self.b.bubble_sort(nums), sorted_nums)

	def test_duplicate_elements(self):
		nums = [5, 5, 1, 1, 3, 11, 11, 6]
		sorted_nums = sorted(nums)

		self.assertEqual(self.b.bubble_sort(nums), sorted_nums)

	def test_empty_list(self):
		nums = []

		self.assertEqual(self.b.bubble_sort(nums), None)


if __name__ == '__main__':
	unittest.main()
