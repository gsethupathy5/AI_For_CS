# Created by asetti2002 at 2024/04/25 20:42
# leetgo: 1.4.3
# https://leetcode.com/problems/diagonal-traverse-ii/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonal_map = {}
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i + j not in diagonal_map:
                    diagonal_map[i + j] = []
                diagonal_map[i + j].append(nums[i][j])
        
        result = []
        for k in sorted(diagonal_map.keys()):
            result.extend(reversed(diagonal_map[k]))
        
        return result
# @lc code=end

if __name__ == "__main__":
    nums: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findDiagonalOrder(nums)
    print("\noutput:", serialize(ans, "integer[]"))
