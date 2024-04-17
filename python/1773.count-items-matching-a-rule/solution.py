# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/count-items-matching-a-rule/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        

# @lc code=end

if __name__ == "__main__":
    items: List[List[str]] = deserialize("List[List[str]]", read_line())
    ruleKey: str = deserialize("str", read_line())
    ruleValue: str = deserialize("str", read_line())
    ans = Solution().countMatches(items, ruleKey, ruleValue)
    print("\noutput:", serialize(ans, "integer"))
