# Created by asetti2002 at 2024/04/17 02:09
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-people-to-teach/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    languages: List[List[int]] = deserialize("List[List[int]]", read_line())
    friendships: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().minimumTeachings(n, languages, friendships)
    print("\noutput:", serialize(ans, "integer"))
