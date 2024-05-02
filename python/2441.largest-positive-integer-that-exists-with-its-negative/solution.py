# Created by asetti2002 at 2024/05/01 20:00
# leetgo: 1.4.3
# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        positives = set(num for num in nums if num >= 0)
        for num in positives:
            if -num in nums:
                return num
        return -1
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findMaxK(nums)
    print("\noutput:", serialize(ans, "integer"))
