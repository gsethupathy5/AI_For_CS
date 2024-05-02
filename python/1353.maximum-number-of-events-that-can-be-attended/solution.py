# Created by asetti2002 at 2024/04/25 20:34
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(reverse=True)
        visited = set()
        count = 0
        
        for start, end in events:
            for day in range(start, end+1):
                if day not in visited:
                    visited.add(day)
                    count += 1
                    break
        
        return count
# @lc code=end

if __name__ == "__main__":
    events: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxEvents(events)
    print("\noutput:", serialize(ans, "integer"))
