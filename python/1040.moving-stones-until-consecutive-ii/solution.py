# Created by asetti2002 at 2024/04/25 19:57
# leetgo: 1.4.3
# https://leetcode.com/problems/moving-stones-until-consecutive-ii/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        n = len(stones)
        
        max_moves = max(stones[n - 1] - stones[1] - n + 2, stones[n - 2] - stones[0] - n + 2)
        
        min_moves = n
        i, j = 0, 0
        
        for i in range(n):
            while j + 1 < n and stones[j + 1] - stones[i] + 1 <= n:
                j += 1
            cost = n - (j - i + 1)
            if j - i + 1 == n - 1 and stones[j] - stones[i] + 1 == n - 1:
                cost = 2
            min_moves = min(min_moves, cost)
        
        return [min_moves, max_moves]
# @lc code=end

if __name__ == "__main__":
    stones: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numMovesStonesII(stones)
    print("\noutput:", serialize(ans, "integer[]"))
