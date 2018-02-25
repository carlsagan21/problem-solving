class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        def plus_reverse(x):
            tmp = []
            while x > 0:
                tmp.append(x % 10)
                x //= 10

            acum = 0
            for idx, digit in enumerate(tmp):
                acum += (10 ** (len(tmp) - idx - 1)) * digit
                if acum >= 2 ** 31:
                    return 0

            return acum

        if x >= 0:
            return plus_reverse(x)
        else:
            return -plus_reverse(-x)
