# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/tree-of-coprimes/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    edges: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().getCoprimes(nums, edges)
    print("\noutput:", serialize(ans, "integer[]"))
