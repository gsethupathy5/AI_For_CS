# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/beautiful-arrangement-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().constructArray(n, k)
    print("\noutput:", serialize(ans, "integer[]"))
