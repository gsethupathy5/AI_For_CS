# Created by asetti2002 at 2024/04/25 20:31
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        total = sum(arr[:k])
        if total / k >= threshold:
            count += 1
        
        for i in range(k, len(arr)):
            total += arr[i] - arr[i - k]
            if total / k >= threshold:
                count += 1
        
        return count
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    threshold: int = deserialize("int", read_line())
    ans = Solution().numOfSubarrays(arr, k, threshold)
    print("\noutput:", serialize(ans, "integer"))
