class Solution:
    # def rotateString(self, A, B):
    #     """
    #     :type A: str
    #     :type B: str
    #     :rtype: bool
    #     """
    #     if len(A) != len(B):
    #         return False

    #     return B in A + A

    #     class Solution:

    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False

        for i in range(len(A)):
            if A[i:] + A[:i] == B:
                return True

        return False
