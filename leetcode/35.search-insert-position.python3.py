class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def searchIdx(nums, target, start_idx):
            if not nums:
                return start_idx

            if len(nums) == 1:
                if target <= nums[0]:
                    return start_idx
                else:
                    return start_idx + 1

            middle = len(nums) // 2
            if nums[middle] == target:
                return start_idx + middle
            elif nums[middle] > target:
                return searchIdx(nums[:middle], target, start_idx)
            else:
                return searchIdx(nums[middle + 1:], target, start_idx + middle + 1)

        return searchIdx(nums, target, 0)
