# Created by asetti2002 at 2024/04/17 02:18
# leetgo: 1.4.3
# https://leetcode.com/problems/integer-to-english-words/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def numberToWords(self, num: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().numberToWords(num)
    print("\noutput:", serialize(ans, "string"))
