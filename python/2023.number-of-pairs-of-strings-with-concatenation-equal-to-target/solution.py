# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    nums: List[str] = deserialize("List[str]", read_line())
    target: str = deserialize("str", read_line())
    ans = Solution().numOfPairs(nums, target)
    print("\noutput:", serialize(ans, "integer"))
