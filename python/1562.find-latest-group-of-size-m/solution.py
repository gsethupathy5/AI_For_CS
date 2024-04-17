# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/find-latest-group-of-size-m/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    m: int = deserialize("int", read_line())
    ans = Solution().findLatestStep(arr, m)
    print("\noutput:", serialize(ans, "integer"))
