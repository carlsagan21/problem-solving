class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"

        last_result = self.countAndSay(n - 1)

        result = ""
        val = last_result[0]
        cnt = 1
        for c in last_result[1:]:
            if val == c:
                cnt += 1
            else:
                result += str(cnt) + val
                val = c
                cnt = 1

        result += str(cnt) + val

        return result
