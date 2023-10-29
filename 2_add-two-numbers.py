# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # adds the two number which are in the linked lists
        numSum = 0
        decimal = 1
        while l1 is not None and l2 is not None:
            numSum += (l1.val + l2.val) * decimal
            decimal *= 10
            l1, l2 = l1.next, l2.next
        current = None
        print(numSum)
        if l1 is None and l2 is not None:
            current = l2
        elif l1 is not None and l2 is None:
            current = l1

        while current is not None:
            numSum += current.val * decimal
            decimal *= 10
            current = current.next

        l3 = ListNode(val=numSum % 10)
        numSum //= 10
        current = l3
        while numSum > 0:
            current.next = ListNode(val=numSum % 10)
            numSum = numSum // 10
            current = current.next
        return l3
