# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/kth-smallest-instructions/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    destination: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kthSmallestPath(destination, k)
    print("\noutput:", serialize(ans, "string"))
