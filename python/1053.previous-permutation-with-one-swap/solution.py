# Created by asetti2002 at 2024/04/25 19:59
# leetgo: 1.4.3
# https://leetcode.com/problems/previous-permutation-with-one-swap/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        def prev_perm_opt1(arr):
            n = len(arr)
            i = n - 2
            while i >= 0 and arr[i] <= arr[i+1]:
                i -= 1
            if i == -1:
                return arr
            j = n - 1
            while arr[j] >= arr[i]:
                j -= 1
            while arr[j] == arr[j-1]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
            return arr
        return prev_perm_opt1(arr)
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().prevPermOpt1(arr)
    print("\noutput:", serialize(ans, "integer[]"))
