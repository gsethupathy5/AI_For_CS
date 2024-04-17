# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    knowledge: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().evaluate(s, knowledge)
    print("\noutput:", serialize(ans, "string"))
