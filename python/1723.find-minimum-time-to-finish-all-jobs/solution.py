# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/find-minimum-time-to-finish-all-jobs/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    jobs: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minimumTimeRequired(jobs, k)
    print("\noutput:", serialize(ans, "integer"))
