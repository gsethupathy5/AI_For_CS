# Created by asetti2002 at 2024/05/01 19:50
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-cycle-in-a-graph/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        longest = 0
        
        for i in range(n):
            current = i
            visited = set()
            length = 0
            
            while current not in visited:
                visited.add(current)
                current = edges[current]
                length += 1
                if current == i:
                    longest = max(longest, length)
                    break
                    
        return longest if longest > 2 else -1
# @lc code=end

if __name__ == "__main__":
    edges: List[int] = deserialize("List[int]", read_line())
    ans = Solution().longestCycle(edges)
    print("\noutput:", serialize(ans, "integer"))
