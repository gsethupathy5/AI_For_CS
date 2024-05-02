# Created by asetti2002 at 2024/04/25 20:27
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        def checkSquareSideLength(matrix, threshold, sideLength):
            return sum(sum(row[j:j + sideLength]) for row in matrix[i:i + sideLength]) <= threshold

        m, n = len(mat), len(mat[0])
        prefixSum = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                prefixSum[i + 1][j + 1] = prefixSum[i + 1][j] + prefixSum[i][j + 1] - prefixSum[i][j] + mat[i][j]

        left, right = 0, min(m, n)
        result = 0

        while left <= right:
            mid = left + (right - left) // 2
            found = False

            for i in range(m - mid + 1):
                for j in range(n - mid + 1):
                    if prefixSum[i + mid][j + mid] - prefixSum[i][j + mid] - prefixSum[i + mid][j] + prefixSum[i][j] <= threshold:
                        found = True
                        break

                if found:
                    break

            if found:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result
# @lc code=end

if __name__ == "__main__":
    mat: List[List[int]] = deserialize("List[List[int]]", read_line())
    threshold: int = deserialize("int", read_line())
    ans = Solution().maxSideLength(mat, threshold)
    print("\noutput:", serialize(ans, "integer"))
