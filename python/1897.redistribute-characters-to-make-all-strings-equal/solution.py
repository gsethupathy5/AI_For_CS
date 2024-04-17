# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    ans = Solution().makeEqual(words)
    print("\noutput:", serialize(ans, "boolean"))
