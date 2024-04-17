# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def average(self, salary: List[int]) -> float:
        

# @lc code=end

if __name__ == "__main__":
    salary: List[int] = deserialize("List[int]", read_line())
    ans = Solution().average(salary)
    print("\noutput:", serialize(ans, "double"))
