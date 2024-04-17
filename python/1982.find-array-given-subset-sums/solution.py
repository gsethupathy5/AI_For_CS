# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/find-array-given-subset-sums/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    sums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().recoverArray(n, sums)
    print("\noutput:", serialize(ans, "integer[]"))
