# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/intervals-between-identical-elements/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().getDistances(arr)
    print("\noutput:", serialize(ans, "long[]"))
