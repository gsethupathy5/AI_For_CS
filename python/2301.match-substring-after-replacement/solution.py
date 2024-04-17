# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/match-substring-after-replacement/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    sub: str = deserialize("str", read_line())
    mappings: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().matchReplacement(s, sub, mappings)
    print("\noutput:", serialize(ans, "boolean"))
