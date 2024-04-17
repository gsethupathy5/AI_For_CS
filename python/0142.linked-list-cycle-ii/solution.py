# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/linked-list-cycle-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    pos: int = deserialize("int", read_line())
    ans = Solution().detectCycle(head, pos)
    print("\noutput:", serialize(ans, "ListNode"))
