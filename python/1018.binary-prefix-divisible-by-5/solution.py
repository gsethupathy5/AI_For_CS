# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/binary-prefix-divisible-by-5/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().prefixesDivBy5(nums)
    print("\noutput:", serialize(ans, "boolean[]"))
