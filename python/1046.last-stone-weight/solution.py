# Created by asetti2002 at 2024/04/25 19:58
# leetgo: 1.4.3
# https://leetcode.com/problems/last-stone-weight/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        stones = [-x for x in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            
            if x != y:
                heapq.heappush(stones, y - x)
        
        return 0 if len(stones) == 0 else -stones[0]
# @lc code=end

if __name__ == "__main__":
    stones: List[int] = deserialize("List[int]", read_line())
    ans = Solution().lastStoneWeight(stones)
    print("\noutput:", serialize(ans, "integer"))
