# Created by asetti2002 at 2024/04/17 02:10
# leetgo: 1.4.3
# https://leetcode.com/problems/count-unhappy-friends/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    preferences: List[List[int]] = deserialize("List[List[int]]", read_line())
    pairs: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().unhappyFriends(n, preferences, pairs)
    print("\noutput:", serialize(ans, "integer"))