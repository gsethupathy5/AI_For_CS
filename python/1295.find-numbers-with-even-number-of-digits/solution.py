# Created by asetti2002 at 2024/04/25 20:27
# leetgo: 1.4.3
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum(1 for num in nums if len(str(num)) % 2 == 0)
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findNumbers(nums)
    print("\noutput:", serialize(ans, "integer"))
