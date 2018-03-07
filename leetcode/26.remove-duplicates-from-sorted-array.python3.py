class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        last_uniq_val_idx = 0
        for n in nums[1:]:
            if nums[last_uniq_val_idx] != n:
                last_uniq_val_idx += 1
                nums[last_uniq_val_idx] = n

        return last_uniq_val_idx + 1
