# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    logs: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().hardestWorker(n, logs)
    print("\noutput:", serialize(ans, "integer"))
