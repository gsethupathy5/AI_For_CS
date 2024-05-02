# Created by asetti2002 at 2024/05/01 19:40
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counts = [0] * 10**9
        for t in tasks:
            counts[t] += 1
        
        rounds = 0
        while sum(counts) > 0:
            two = 0
            three = 0
            for i in range(1, len(counts)):
                if counts[i] >= 3:
                    counts[i] -= 3
                    three += 1
                elif counts[i] == 2:
                    counts[i] -= 2
                    two += 1
                elif counts[i] == 1:
                    counts[i] -= 1
            rounds += 1
            if two > 0:
                rounds += 1
            elif three > 0:
                rounds += 1
        
        return rounds if sum(counts) == 0 else -1
# @lc code=end

if __name__ == "__main__":
    tasks: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumRounds(tasks)
    print("\noutput:", serialize(ans, "integer"))
