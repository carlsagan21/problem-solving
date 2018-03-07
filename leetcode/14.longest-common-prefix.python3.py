class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        longest = strs[0]
        for s in strs[1:]:
            for c_idx, c_pair in enumerate(zip(longest, s)):
                if c_pair[0] != c_pair[1]:
                    longest = longest[:c_idx]
                    break

            if len(s) < len(longest):
                longest = s

        return longest
