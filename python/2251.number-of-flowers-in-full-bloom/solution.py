# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-flowers-in-full-bloom/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    flowers: List[List[int]] = deserialize("List[List[int]]", read_line())
    people: List[int] = deserialize("List[int]", read_line())
    ans = Solution().fullBloomFlowers(flowers, people)
    print("\noutput:", serialize(ans, "integer[]"))
