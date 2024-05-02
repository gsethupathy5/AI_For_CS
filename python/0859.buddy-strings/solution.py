# Created by asetti2002 at 2024/04/25 19:31
# leetgo: 1.4.3
# https://leetcode.com/problems/buddy-strings/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        if s == goal and len(set(s)) < len(s):
            return True
        
        diff = [(a, b) for a, b in zip(s, goal) if a != b]
        
        return len(diff) == 2 and diff[0] == diff[1][::-1]
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    goal: str = deserialize("str", read_line())
    ans = Solution().buddyStrings(s, goal)
    print("\noutput:", serialize(ans, "boolean"))
