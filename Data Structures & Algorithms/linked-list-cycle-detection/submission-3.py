# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or head.next == None or head.next.next == None:
            return False
        hashset = set([(head.val,head.next.val)])
        cur = head
        while cur.next and cur.next.next:
            if (cur.next.val, cur.next.next.val) in hashset:
                return True
            else:
                hashset.add((cur.next.val, cur.next.next.val))
                cur = cur.next
        return False
            