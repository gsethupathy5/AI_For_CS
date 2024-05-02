# Created by asetti2002 at 2024/05/01 19:55
# leetgo: 1.4.3
# https://leetcode.com/problems/check-distances-between-same-letters/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        def dfs(s, distance, index, curDist):
            if index == 26:
                return True
            if distance[index] == 0:
                return dfs(s, distance, index + 1, 0)
            
            for i in range(len(s)):
                if s[i] == chr(97 + index):
                    if curDist == distance[index]:
                        if dfs(s, distance, index + 1, 0):
                            return True
                    elif curDist < distance[index]:
                        if dfs(s, distance, index, curDist + 1):
                            return True
            return False
        
        return dfs(s, distance, 0, 0)
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    distance: List[int] = deserialize("List[int]", read_line())
    ans = Solution().checkDistances(s, distance)
    print("\noutput:", serialize(ans, "boolean"))
