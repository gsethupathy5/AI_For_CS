# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/copy-list-with-random-pointer/

from typing import *
from leetgo_py import *

# @lc code=begin

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().copyRandomList(head)
    print("\noutput:", serialize(ans, "ListNode"))
