# Created by asetti2002 at 2024/04/25 20:42
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        window = n - k
        total_sum = sum(cardPoints)
        min_sum = sum(cardPoints[:window])
        curr_sum = min_sum
        
        for i in range(window, n):
            curr_sum += cardPoints[i] - cardPoints[i - window]
            min_sum = min(min_sum, curr_sum)
            
        return total_sum - min_sum
# @lc code=end

if __name__ == "__main__":
    cardPoints: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxScore(cardPoints, k)
    print("\noutput:", serialize(ans, "integer"))
