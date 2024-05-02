# Created by asetti2002 at 2024/05/01 20:20
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-impossible-or/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        result = 1
        while True:
            if result not in nums:
                return result
            result += 1
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minImpossibleOR(nums)
    print("\noutput:", serialize(ans, "integer"))
