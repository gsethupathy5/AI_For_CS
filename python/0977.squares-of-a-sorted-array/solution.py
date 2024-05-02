# Created by asetti2002 at 2024/04/25 19:48
# leetgo: 1.4.3
# https://leetcode.com/problems/squares-of-a-sorted-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([num*num for num in nums])
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sortedSquares(nums)
    print("\noutput:", serialize(ans, "integer[]"))
