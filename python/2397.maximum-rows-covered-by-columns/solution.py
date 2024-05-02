# Created by asetti2002 at 2024/05/01 19:56
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-rows-covered-by-columns/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        def count_covered(matrix, selected):
            count = 0
            for row in matrix:
                if all(row[i] == 0 or i in selected for i in range(len(row))):
                    count += 1
            return count
        
        def backtrack(index, selected, numSelect):
            if len(selected) == numSelect:
                return count_covered(matrix, selected)
            
            if index == len(matrix[0]):
                return 0
            
            select_column = backtrack(index + 1, selected + [index], numSelect)
            skip_column = backtrack(index + 1, selected, numSelect)
            return max(select_column, skip_column)
        
        return backtrack(0, [], numSelect)
# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    numSelect: int = deserialize("int", read_line())
    ans = Solution().maximumRows(matrix, numSelect)
    print("\noutput:", serialize(ans, "integer"))
