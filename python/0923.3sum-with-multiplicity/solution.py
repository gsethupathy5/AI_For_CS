# Created by asetti2002 at 2024/04/25 19:40
# leetgo: 1.4.3
# https://leetcode.com/problems/3sum-with-multiplicity/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10**9 + 7
        count = [0] * 101
        for i in arr:
            count[i] += 1
        res = 0
        for i in range(101):
            for j in range(i, 101):
                k = target - i - j
                if k < 0 or k > 100:
                    continue
                if i == j == k:
                    res += count[i] * (count[i] - 1) * (count[i] - 2) // 6
                elif i == j:
                    res += count[i] * (count[i] - 1) // 2 * count[k]
                elif j < k:
                    res += count[i] * count[j] * count[k]
        return res % MOD
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().threeSumMulti(arr, target)
    print("\noutput:", serialize(ans, "integer"))
