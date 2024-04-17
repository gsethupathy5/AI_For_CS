# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/merge-in-between-linked-lists/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    list1: ListNode = deserialize("ListNode", read_line())
    a: int = deserialize("int", read_line())
    b: int = deserialize("int", read_line())
    list2: ListNode = deserialize("ListNode", read_line())
    ans = Solution().mergeInBetween(list1, a, b, list2)
    print("\noutput:", serialize(ans, "ListNode"))
