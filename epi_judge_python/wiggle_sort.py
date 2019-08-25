class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1):
          nums[i:i + 2] = sorted(nums[i:i + 2], reverse = i % 2)