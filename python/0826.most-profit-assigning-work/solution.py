# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/most-profit-assigning-work/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    difficulty: List[int] = deserialize("List[int]", read_line())
    profit: List[int] = deserialize("List[int]", read_line())
    worker: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfitAssignment(difficulty, profit, worker)
    print("\noutput:", serialize(ans, "integer"))
