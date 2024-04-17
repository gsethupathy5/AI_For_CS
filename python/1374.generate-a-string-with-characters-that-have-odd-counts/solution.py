# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def generateTheString(self, n: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().generateTheString(n)
    print("\noutput:", serialize(ans, "string"))
