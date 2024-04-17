# Created by asetti2002 at 2024/04/17 02:17
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    dictionary: List[str] = deserialize("List[str]", read_line())
    ans = Solution().findLongestWord(s, dictionary)
    print("\noutput:", serialize(ans, "string"))
