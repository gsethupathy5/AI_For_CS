# Created by asetti2002 at 2024/04/25 20:34
# leetgo: 1.4.3
# https://leetcode.com/problems/construct-target-array-with-multiple-sums/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        import heapq
        
        heap = [-x for x in target]
        heapq.heapify(heap)
        total = sum(target)
        
        while True:
            largest = -heapq.heappop(heap)
            total -= largest
            if largest == 1 or total == 1:
                return largest == 1 or total == 1
            if largest < total or total == 0 or largest % total == 0:
                return False
            largest %= total
            total += largest
            heapq.heappush(heap, -largest)
# @lc code=end

if __name__ == "__main__":
    target: List[int] = deserialize("List[int]", read_line())
    ans = Solution().isPossible(target)
    print("\noutput:", serialize(ans, "boolean"))
