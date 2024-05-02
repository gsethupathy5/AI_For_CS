# Created by asetti2002 at 2024/04/25 19:02
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-matrix-sum/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        negatives = 0
        min_abs = float('inf')
        total_sum = 0
        
        for row in matrix:
            for num in row:
                total_sum += abs(num)
                if num < 0:
                    negatives += 1
                min_abs = min(min_abs, abs(num))
        
        return total_sum if negatives % 2 == 0 else total_sum - 2 * min_abs
# @lc code=end

if __name__ == "__main__":
    matrix: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxMatrixSum(matrix)
    print("\noutput:", serialize(ans, "long"))
