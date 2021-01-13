# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        sentinel = ListNode(-1, head)
        slow, fast = sentinel, head
        while fast:
            while fast.val == fast.next.val:
                fast = fast.next
            if slow.next == fast:
                slow = slow.next
            else:
                slow.next = fast.next
            fast = fast.next
        return sentinel.next

# Time complexity: $O(n)$.
# Space complexity: $O(1)$.
