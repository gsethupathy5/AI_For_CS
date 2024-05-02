# Created by asetti2002 at 2024/04/25 20:14
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-absolute-difference/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = float('inf')
        result = []
        
        for i in range(len(arr) - 1):
            diff = arr[i+1] - arr[i]
            if diff < min_diff:
                min_diff = diff
                result = [[arr[i], arr[i+1]]]
            elif diff == min_diff:
                result.append([arr[i], arr[i+1]])
        
        return result
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumAbsDifference(arr)
    print("\noutput:", serialize(ans, "integer[][]"))
