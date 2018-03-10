class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == "":
            return 0

        for idx, char in (enumerate(haystack[:-(len(needle) - 1)]) if not len(needle) == 1 else enumerate(haystack)):
            if haystack[idx:idx + len(needle)] == needle:
                return idx

        return -1
