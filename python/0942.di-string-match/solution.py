# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/di-string-match/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().diStringMatch(s)
    print("\noutput:", serialize(ans, "integer[]"))
