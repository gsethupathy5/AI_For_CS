# Created by asetti2002 at 2024/04/17 02:19
# leetgo: 1.4.3
# https://leetcode.com/problems/combination-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    candidates: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().combinationSum(candidates, target)
    print("\noutput:", serialize(ans, "integer[][]"))
