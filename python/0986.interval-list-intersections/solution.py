# Created by asetti2002 at 2024/04/25 19:50
# leetgo: 1.4.3
# https://leetcode.com/problems/interval-list-intersections/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i, j = 0, 0
        
        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            
            if start <= end:
                result.append([start, end])
                
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
                
        return result
# @lc code=end

if __name__ == "__main__":
    firstList: List[List[int]] = deserialize("List[List[int]]", read_line())
    secondList: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().intervalIntersection(firstList, secondList)
    print("\noutput:", serialize(ans, "integer[][]"))
