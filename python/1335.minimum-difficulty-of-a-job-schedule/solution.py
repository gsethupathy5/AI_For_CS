# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    jobDifficulty: List[int] = deserialize("List[int]", read_line())
    d: int = deserialize("int", read_line())
    ans = Solution().minDifficulty(jobDifficulty, d)
    print("\noutput:", serialize(ans, "integer"))