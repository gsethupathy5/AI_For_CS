# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxScoreIndices(nums)
    print("\noutput:", serialize(ans, "integer[]"))
