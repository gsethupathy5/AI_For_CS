# Created by asetti2002 at 2024/04/25 19:27
# leetgo: 1.4.3
# https://leetcode.com/problems/positions-of-large-groups/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        start = 0
        for i in range(len(s)):
            if i == len(s) - 1 or s[i] != s[i + 1]:
                if i - start >= 2:
                    result.append([start, i])
                start = i + 1
        return result
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().largeGroupPositions(s)
    print("\noutput:", serialize(ans, "integer[][]"))
