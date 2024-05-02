# Created by asetti2002 at 2024/04/25 19:53
# leetgo: 1.4.3
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = 0
        remainder_dict = collections.defaultdict(int)
        
        for t in time:
            remainder = t % 60
            count += remainder_dict[(60 - remainder) % 60]
            remainder_dict[remainder] += 1
        
        return count
# @lc code=end

if __name__ == "__main__":
    time: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numPairsDivisibleBy60(time)
    print("\noutput:", serialize(ans, "integer"))
