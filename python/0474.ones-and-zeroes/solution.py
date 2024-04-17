# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/ones-and-zeroes/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().findMaxForm(strs, m, n)
    print("\noutput:", serialize(ans, "integer"))
