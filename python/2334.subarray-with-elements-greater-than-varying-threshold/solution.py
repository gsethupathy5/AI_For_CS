# Created by asetti2002 at 2024/05/01 19:48
# leetgo: 1.4.3
# https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        def check_subarray(arr, threshold, k):
            for i in range(len(arr)-k+1):
                if min(arr[i:i+k]) > threshold/k:
                    return True
            return False
        
        for k in range(1, len(nums)+1):
            if check_subarray(nums, threshold, k):
                return k
        return -1
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    threshold: int = deserialize("int", read_line())
    ans = Solution().validSubarraySize(nums, threshold)
    print("\noutput:", serialize(ans, "integer"))
