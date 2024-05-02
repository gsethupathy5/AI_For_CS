# Created by asetti2002 at 2024/04/25 19:54
# leetgo: 1.4.3
# https://leetcode.com/problems/binary-prefix-divisible-by-5/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        val = 0
        for num in nums:
            val = (val * 2 + num) % 5
            result.append(val == 0)
        return result
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().prefixesDivBy5(nums)
    print("\noutput:", serialize(ans, "boolean[]"))
