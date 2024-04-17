# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().findBestValue(arr, target)
    print("\noutput:", serialize(ans, "integer"))
