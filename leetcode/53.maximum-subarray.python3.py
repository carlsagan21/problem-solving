class Solution:
    # List[int] -> int
    def maxSubArrayBF(self, nums):
        # Algorithm 1: Brute Force
        maxSumSoFar = nums[0]
        # maxISoFar = 0
        # maxJSoFar = 0
        for i, _ in enumerate(nums):
            sum = 0
            for _, m in enumerate(nums[i:]):
                sum += m
                if sum > maxSumSoFar:
                    maxSumSoFar = sum
                    # maxISoFar = i
                    # maxJSoFar = j

        return maxSumSoFar  # , (i, j)

    # List[int] -> int
    # TODO 이해가 잘 안됨... prefix
    def maxSubArrayDC(self, nums):
        # Algorithm 2: Divide and Conquer
        # Array of cumulative sums allows for the computation of overlapping solution in constant time.
        sums = [0]
        for n in nums:
            sums.append(sums[-1] + n)

        def loop(l, r):
            if l == r:
                return nums[l], sums[l], sums[l + 1]
            else:
                # If I have more than one element, split the array and loop over left and right part.
                c = (l + r - 1) // 2
                resLeft, minPrefixLeft, maxPrefixLeft = loop(l, c)
                resRight, minPrefixRight, maxPrefixRight = loop(c + 1, r)
                minPrefix = min(minPrefixLeft, minPrefixRight)
                maxPrefix = max(maxPrefixLeft, maxPrefixRight)
                # Solution overlapping both the left and the right part can be computed as follows.
                resCenter = maxPrefixRight - minPrefixLeft
                # Overall solution is maximum of solutions on the left, on the right and overlapping.
                res = max(resLeft, resCenter, resRight)
                return res, minPrefix, maxPrefix

        res, _, _ = loop(0, len(nums) - 1)

        return res

    # List[int] -> int
    def maxSubArrayDP(self, nums):
        # Algorithm 3: Dynamic Programming
        max_ending_here = max_so_far = nums[0]
        for x in nums[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far


s = Solution()
print(s.maxSubArrayDC([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
