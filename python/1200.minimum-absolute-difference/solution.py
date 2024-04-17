# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-absolute-difference/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumAbsDifference(arr)
    print("\noutput:", serialize(ans, "integer[][]"))
