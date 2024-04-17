# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/combination-sum-iii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().combinationSum3(k, n)
    print("\noutput:", serialize(ans, "integer[][]"))
