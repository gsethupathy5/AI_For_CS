# Created by asetti2002 at 2024/04/25 19:25
# leetgo: 1.4.3
# https://leetcode.com/problems/most-profit-assigning-work/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        from bisect import bisect_right
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        max_profit = 0
        curr_max = 0
        i = 0
        for ability in worker:
            while i < len(jobs) and jobs[i][0] <= ability:
                curr_max = max(curr_max, jobs[i][1])
                i += 1
            max_profit += curr_max
        return max_profit
# @lc code=end

if __name__ == "__main__":
    difficulty: List[int] = deserialize("List[int]", read_line())
    profit: List[int] = deserialize("List[int]", read_line())
    worker: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfitAssignment(difficulty, profit, worker)
    print("\noutput:", serialize(ans, "integer"))
