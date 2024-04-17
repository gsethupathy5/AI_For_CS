# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/determine-if-two-events-have-conflict/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        

# @lc code=end

if __name__ == "__main__":
    event1: List[str] = deserialize("List[str]", read_line())
    event2: List[str] = deserialize("List[str]", read_line())
    ans = Solution().haveConflict(event1, event2)
    print("\noutput:", serialize(ans, "boolean"))
