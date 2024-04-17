# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/linked-list-random-node/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        

    def getRandom(self) -> int:
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

# @lc code=end

if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    constructor_params = split_array(params[0])
    head: ListNode = deserialize("ListNode", constructor_params[0])
    obj = Solution(head)

    for i in range(1, len(ops)):
        match ops[i]:
            case "getRandom":
                ans = serialize(obj.getRandom())
                output.append(ans)

    print("\noutput:", join_array(output))
