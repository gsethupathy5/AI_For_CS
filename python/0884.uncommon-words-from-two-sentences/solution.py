# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/uncommon-words-from-two-sentences/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    s1: str = deserialize("str", read_line())
    s2: str = deserialize("str", read_line())
    ans = Solution().uncommonFromSentences(s1, s2)
    print("\noutput:", serialize(ans, "string[]"))
