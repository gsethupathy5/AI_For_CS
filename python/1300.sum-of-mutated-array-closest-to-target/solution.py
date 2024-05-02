# Created by asetti2002 at 2024/04/25 20:06
# leetgo: 1.4.3
# https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)
        l, r = 0, max(arr)
        while l < r:
            mid = (l + r) // 2
            index = bisect_left(arr, mid)
            cur = prefix[index] + (n - index) * mid
            if cur < target:
                l = mid + 1
            else:
                r = mid
        if abs(prefix[bisect_left(arr, l)] + (n - bisect_left(arr, l)) * l - target) < abs(prefix[bisect_left(arr, l) - 1] + (n - bisect_left(arr, l) + 1) * l - target):
            return l
        else:
            return l - 1
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().findBestValue(arr, target)
    print("\noutput:", serialize(ans, "integer"))
