class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        acc_strs = [""]
        for c in S:
            if c.isalpha():
                acc_strs = [acc_str + c_ul for acc_str in acc_strs for c_ul in [
                    c.upper(), c.lower()]]
            else:
                acc_strs = [acc_str + c for acc_str in acc_strs]

        return acc_strs

    # def letterCasePermutation(self, S):
    #     """
    #     :type S: str
    #     :rtype: List[str]
    #     """
    #     acc_strs = [""]
    #     for c in S:
    #         if c.isalpha():
    #             temp_acc_strs = []
    #             for idx, acc_str in enumerate(acc_strs):
    #                 acc_strs[idx] = "".join([acc_str, c])
    #                 temp_acc_strs.append(
    #                     "".join([acc_str, c.lower() if c.isupper() else c.upper()]))
    #             acc_strs.extend(temp_acc_strs)
    #         else:
    #             for idx, acc_str in enumerate(acc_strs):
    #                 acc_strs[idx] = "".join([acc_str, c])

    #     return acc_strs
