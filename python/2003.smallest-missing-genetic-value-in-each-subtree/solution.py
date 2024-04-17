# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/smallest-missing-genetic-value-in-each-subtree/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    parents: List[int] = deserialize("List[int]", read_line())
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().smallestMissingValueSubtree(parents, nums)
    print("\noutput:", serialize(ans, "integer[]"))
