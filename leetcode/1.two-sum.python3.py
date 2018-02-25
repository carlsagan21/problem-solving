class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ht = {}
        for i, n in enumerate(nums):
            compliment = target - n
            if compliment in ht:
                return [ht[compliment], i]
            ht[n] = i
