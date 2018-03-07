# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        start_node = ListNode(-1)
        last_node = start_node
        while l1 or l2:
            if not l1:
                last_node.next = l2
                break
            if not l2:
                last_node.next = l1
                break

            if l1.val < l2.val:
                last_node.next = l1
                l1 = l1.next
            else:
                last_node.next = l2
                l2 = l2.next
            last_node = last_node.next

        return start_node.next
