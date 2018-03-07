class Solution:
    def _get_next_idxs(self, nums, val, front_val_idx, back_non_val_idx):
        front_val_idx += 1
        back_non_val_idx -= 1
        while front_val_idx < len(nums) and nums[front_val_idx] != val:
            front_val_idx += 1
        while back_non_val_idx >= 0 and nums[back_non_val_idx] == val:
            back_non_val_idx -= 1
        return front_val_idx, back_non_val_idx

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        front_val_idx, back_non_val_idx = self._get_next_idxs(
            nums, val, -1, len(nums))

        while front_val_idx < back_non_val_idx:
            nums[front_val_idx] = nums[back_non_val_idx]
            front_val_idx, back_non_val_idx = self._get_next_idxs(
                nums, val, front_val_idx, back_non_val_idx)

        return back_non_val_idx + 1
