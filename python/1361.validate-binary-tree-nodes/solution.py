# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/validate-binary-tree-nodes/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    leftChild: List[int] = deserialize("List[int]", read_line())
    rightChild: List[int] = deserialize("List[int]", read_line())
    ans = Solution().validateBinaryTreeNodes(n, leftChild, rightChild)
    print("\noutput:", serialize(ans, "boolean"))
