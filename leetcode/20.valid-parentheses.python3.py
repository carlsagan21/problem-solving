class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif c == ')' and (not stack or stack.pop() != '('):
                return False
            elif c == '}' and (not stack or stack.pop() != '{'):
                return False
            elif c == ']' and (not stack or stack.pop() != '['):  # c == ']'
                return False

        return not stack
