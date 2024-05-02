# Created by asetti2002 at 2024/04/25 20:12
# leetgo: 1.4.3
# https://leetcode.com/problems/make-array-strictly-increasing/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        import bisect
        
        dp = {-1: 0}
        arr2.sort()
        
        for n in arr1:
            tmp = {}
            for key in dp:
                if n > key:
                    tmp[n] = min(tmp.get(n, float('inf')), dp[key])
                i = bisect.bisect_right(arr2, key)
                if i < len(arr2):
                    tmp[arr2[i]] = min(tmp.get(arr2[i], float('inf')), dp[key] + 1)
            dp = tmp
        
        if dp:
            return min(dp.values())
        else:
            return -1
# @lc code=end

if __name__ == "__main__":
    arr1: List[int] = deserialize("List[int]", read_line())
    arr2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().makeArrayIncreasing(arr1, arr2)
    print("\noutput:", serialize(ans, "integer"))
