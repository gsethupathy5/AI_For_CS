# Created by asetti2002 at 2024/04/17 02:07
# leetgo: 1.4.3
# https://leetcode.com/problems/parallel-courses-iii/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    relations: List[List[int]] = deserialize("List[List[int]]", read_line())
    time: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumTime(n, relations, time)
    print("\noutput:", serialize(ans, "integer"))
