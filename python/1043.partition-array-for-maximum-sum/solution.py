# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/partition-array-for-maximum-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxSumAfterPartitioning(arr, k)
    print("\noutput:", serialize(ans, "integer"))
