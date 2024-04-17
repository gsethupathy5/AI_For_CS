# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/rearrange-characters-to-make-target-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    target: str = deserialize("str", read_line())
    ans = Solution().rearrangeCharacters(s, target)
    print("\noutput:", serialize(ans, "integer"))
