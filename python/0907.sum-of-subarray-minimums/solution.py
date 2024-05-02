# Created by asetti2002 at 2024/04/25 19:38
# leetgo: 1.4.3
# https://leetcode.com/problems/sum-of-subarray-minimums/

from typing import *
from leetgo_py import *

# @lc code=begin
from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        stack = []
        res = 0
        arr = [0] + arr + [0]
        for i, num in enumerate(arr):
            while stack and arr[stack[-1]] > num:
                j = stack.pop()
                k = stack[-1]
                res += arr[j] * (i - j) * (j - k)
            stack.append(i)
        return res % mod
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sumSubarrayMins(arr)
    print("\noutput:", serialize(ans, "integer"))
