# Created by asetti2002 at 2024/04/25 20:38
# leetgo: 1.4.3
# https://leetcode.com/problems/count-number-of-teams/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for i in range(len(rating)):
            for j in range(i+1, len(rating)):
                for k in range(j+1, len(rating)):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        count += 1
        return count
# @lc code=end

if __name__ == "__main__":
    rating: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numTeams(rating)
    print("\noutput:", serialize(ans, "integer"))
