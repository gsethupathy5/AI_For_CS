# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    target: List[int] = deserialize("List[int]", read_line())
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minOperations(target, arr)
    print("\noutput:", serialize(ans, "integer"))
