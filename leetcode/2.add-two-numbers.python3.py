# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, ln1, ln2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_node = ListNode(0)
        last_node = dummy_node
        carry = 0
        while ln1 or ln2:
            if ln1:
                ln1_val = ln1.val
                ln1 = ln1.next
            else:
                ln1_val = 0

            if ln2:
                ln2_val = ln2.val
                ln2 = ln2.next
            else:
                ln2_val = 0

            digit_sum = ln1_val + ln2_val + carry
            carry = digit_sum // 10
            remain = digit_sum % 10
            curr_node = ListNode(remain)
            last_node.next = curr_node
            last_node = curr_node

        # 둘 다 끝났기 때문에, carry만 남은 것.
        # carry가 1이면 하나 달아줘야함.
        if carry == 1:
            last_node.next = ListNode(1)

        return dummy_node.next
