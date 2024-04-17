# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/verifying-an-alien-dictionary/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    order: str = deserialize("str", read_line())
    ans = Solution().isAlienSorted(words, order)
    print("\noutput:", serialize(ans, "boolean"))
