# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().removeZeroSumSublists(head)
    print("\noutput:", serialize(ans, "ListNode"))
