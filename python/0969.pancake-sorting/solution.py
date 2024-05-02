# Created by asetti2002 at 2024/04/25 19:47
# leetgo: 1.4.3
# https://leetcode.com/problems/pancake-sorting/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        for x in range(n, 1, -1):
            idx = arr.index(x)
            if idx == x - 1:
                continue
            if idx != 0:
                res.append(idx + 1)
                arr = arr[:idx+1][::-1] + arr[idx+1:]
            res.append(x)
            arr = arr[:x][::-1] + arr[x:]
        return res
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().pancakeSort(arr)
    print("\noutput:", serialize(ans, "integer[]"))
