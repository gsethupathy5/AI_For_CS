# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/camelcase-matching/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        

# @lc code=end

if __name__ == "__main__":
    queries: List[str] = deserialize("List[str]", read_line())
    pattern: str = deserialize("str", read_line())
    ans = Solution().camelMatch(queries, pattern)
    print("\noutput:", serialize(ans, "boolean[]"))
