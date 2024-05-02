# Created by asetti2002 at 2024/04/25 19:48
# leetgo: 1.4.3
# https://leetcode.com/problems/longest-turbulent-subarray/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        N = len(arr)
        inc = dec = res = 1
        
        for i in range(1, N):
            if arr[i] > arr[i - 1]:
                inc = dec + 1
                dec = 1
            elif arr[i] < arr[i - 1]:
                dec = inc + 1
                inc = 1
            else:
                inc = dec = 1
            res = max(res, max(inc, dec))
        
        return res
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxTurbulenceSize(arr)
    print("\noutput:", serialize(ans, "integer"))
