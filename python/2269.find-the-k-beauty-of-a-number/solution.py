# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/find-the-k-beauty-of-a-number/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().divisorSubstrings(num, k)
    print("\noutput:", serialize(ans, "integer"))