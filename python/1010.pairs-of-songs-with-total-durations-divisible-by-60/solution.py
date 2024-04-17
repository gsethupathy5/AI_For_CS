# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    time: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numPairsDivisibleBy60(time)
    print("\noutput:", serialize(ans, "integer"))
