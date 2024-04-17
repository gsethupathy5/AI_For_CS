# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/interval-list-intersections/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    firstList: List[List[int]] = deserialize("List[List[int]]", read_line())
    secondList: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().intervalIntersection(firstList, secondList)
    print("\noutput:", serialize(ans, "integer[][]"))
