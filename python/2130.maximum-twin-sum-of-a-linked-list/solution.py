# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().pairSum(head)
    print("\noutput:", serialize(ans, "integer"))
