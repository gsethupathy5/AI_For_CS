# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/circular-permutation-in-binary-representation/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    start: int = deserialize("int", read_line())
    ans = Solution().circularPermutation(n, start)
    print("\noutput:", serialize(ans, "integer[]"))
