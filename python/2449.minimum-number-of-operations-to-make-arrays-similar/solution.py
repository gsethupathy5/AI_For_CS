# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-operations-to-make-arrays-similar/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: List[int] = deserialize("List[int]", read_line())
    ans = Solution().makeSimilar(nums, target)
    print("\noutput:", serialize(ans, "long"))