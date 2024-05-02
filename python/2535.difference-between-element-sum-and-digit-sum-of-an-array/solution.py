# Created by asetti2002 at 2024/05/01 20:12
# leetgo: 1.4.3
# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return abs(sum(nums) - sum(int(j) for i in nums for j in str(i)) )
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().differenceOfSum(nums)
    print("\noutput:", serialize(ans, "integer"))
