import random
import unittest


class QuickSort:
    """ Two implementations of quick sort"""

    def left_key_quick_sort(self, nums, left, right):
        """
        Use the leftmost element as the key
        Start comparing from the right
        """
        if left >= right:
            return 
        
        high = right
        low = left
        key = nums[low]

        while left < right:
            while nums[right] > key and left < right:
                right -= 1
            nums[left] = nums[right]

            while nums[left] <= key and left < right:
                left += 1
            nums[right] = nums[left]

        nums[left] = key

        self.left_key_quick_sort(nums, low, left - 1)
        self.left_key_quick_sort(nums, left + 1, high)

        return nums

    def quick_sort(self, nums, left, right):
        if left >= right:
            return
        
        high = right
        low = left
        key = nums[low]

        while left < right:
            while nums[right] > key and left < right:
                right -= 1
            
            while nums[left] <= key and left < right:
                left += 1
            
            nums[left], nums[right] = nums[right], nums[left]
        
        nums[low], nums[left] = nums[left], nums[low]

        self.quick_sort(nums, low, left - 1)
        self.quick_sort(nums, left + 1, high)

        return nums
    


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.q = QuickSort()

    def test_regular_elements(self):
        nums = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
        sorted_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        self.assertEqual(self.q.left_key_quick_sort(nums, 0, len(nums) - 1),
                         sorted_nums)
        self.assertEqual(self.q.quick_sort(nums, 0, len(nums) - 1),
                         sorted_nums)

    # def test_duplicate_elements(self):
    #     nums = [9, 9, 1, 19, 22, 1, 5]
    #     sorted_nums = [1, 1, 5, 9, 9, 19, 22]

    #     self.assertEqual(self.q.left_key_quick_sort(nums, 0, len(nums) - 1),
    #                      sorted_nums)

    #     self.assertEqual(self.q.right_key_quick_sort(nums, 0, len(nums) - 1),
    #                      sorted_nums)

    # def test_empty_list(self):
    #     nums = []

    #     self.assertEqual(self.q.left_key_quick_sort(nums, 0, len(nums) - 1),
    #                      None)

    #     self.assertEqual(self.q.right_key_quick_sort(nums, 0, len(nums) - 1),
    #                      None)

    # def test_all_same_elements(self):
    #     nums = [9, 9, 9, 9, 9]

    #     self.assertEqual(self.q.left_key_quick_sort(nums, 0, len(nums) - 1),
    #                      nums)

    #     self.assertEqual(self.q.right_key_quick_sort(nums, 0, len(nums) - 1),
    #                      nums)

    # def test_large_set_of_elements(self):
    #     nums = [random.randrange(1, 101, 1) for _ in range(100)]
    #     sorted_nums = sorted(nums)

    #     self.assertEqual(self.q.left_key_quick_sort(nums, 0, len(nums) - 1),
    #                      sorted_nums)

    #     self.assertEqual(self.q.right_key_quick_sort(nums, 0, len(nums) - 1),
    #                      sorted_nums)


if __name__ == '__main__':
    unittest.main()

