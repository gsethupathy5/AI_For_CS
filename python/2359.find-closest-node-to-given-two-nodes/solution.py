# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/find-closest-node-to-given-two-nodes/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    edges: List[int] = deserialize("List[int]", read_line())
    node1: int = deserialize("int", read_line())
    node2: int = deserialize("int", read_line())
    ans = Solution().closestMeetingNode(edges, node1, node2)
    print("\noutput:", serialize(ans, "integer"))
