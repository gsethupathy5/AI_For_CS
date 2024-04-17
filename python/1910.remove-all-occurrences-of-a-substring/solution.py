# Created by asetti2002 at 2024/04/17 02:08
# leetgo: 1.4.3
# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    part: str = deserialize("str", read_line())
    ans = Solution().removeOccurrences(s, part)
    print("\noutput:", serialize(ans, "string"))
