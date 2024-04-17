# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-unique-good-subsequences/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    binary: str = deserialize("str", read_line())
    ans = Solution().numberOfUniqueGoodSubsequences(binary)
    print("\noutput:", serialize(ans, "integer"))
