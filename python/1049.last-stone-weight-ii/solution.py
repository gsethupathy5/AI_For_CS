# Created by asetti2002 at 2024/04/25 19:59
# leetgo: 1.4.3
# https://leetcode.com/problems/last-stone-weight-ii/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        dp = {0}
        total = sum(stones)
        
        for stone in stones:
            new_dp = set()
            for weight in dp:
                new_dp.add(weight + stone)
                new_dp.add(abs(weight - stone))
            dp = new_dp
        
        min_weight = float("inf")
        for weight in dp:
            min_weight = min(min_weight, abs(total - 2 * weight))
        
        return min_weight
# @lc code=end

if __name__ == "__main__":
    stones: List[int] = deserialize("List[int]", read_line())
    ans = Solution().lastStoneWeightII(stones)
    print("\noutput:", serialize(ans, "integer"))
