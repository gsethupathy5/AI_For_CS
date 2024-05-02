# Created by asetti2002 at 2024/04/25 20:11
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        dp_fwd, dp_bwd = [0] * n, [0] * n
        for i, a in enumerate(arr):
            dp_fwd[i] = a + dp_fwd[i - 1] if i > 0 else a
        for i in range(n-1, -1, -1):
            dp_bwd[i] = arr[i] + dp_bwd[i + 1] if i < n - 1 else arr[i]
        return max(max(dp_fwd), max(dp_bwd), max(dp_fwd[i - 1] + dp_bwd[i + 1] for i in range(1, n - 1)))
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumSum(arr)
    print("\noutput:", serialize(ans, "integer"))
