# Created by asetti2002 at 2024/05/01 20:01
# leetgo: 1.4.3
# https://leetcode.com/problems/determine-if-two-events-have-conflict/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        start1, end1 = event1
        start2, end2 = event2
        return start1 <= end2 and start2 <= end1
# @lc code=end

if __name__ == "__main__":
    event1: List[str] = deserialize("List[str]", read_line())
    event2: List[str] = deserialize("List[str]", read_line())
    ans = Solution().haveConflict(event1, event2)
    print("\noutput:", serialize(ans, "boolean"))
