# Created by asetti2002 at 2024/04/17 02:11
# leetgo: 1.4.3
# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().getHappyString(n, k)
    print("\noutput:", serialize(ans, "string"))
