# Created by asetti2002 at 2024/04/25 20:12
# leetgo: 1.4.3
# https://leetcode.com/problems/k-concatenation-maximum-sum/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 1000000007
        def max_subarray_sum(arr):
            max_ending_here = max_so_far = 0
            for x in arr:
                max_ending_here = max(x, max_ending_here + x)
                max_so_far = max(max_so_far, max_ending_here)
            return max_so_far
        
        max_sum = max_subarray_sum(arr * 2)
        if k == 1:
            return max_sum
        
        prefix_sum = sum(arr)
        suffix_sum = sum(arr)
        total_sum = sum(arr) * k
        
        if total_sum > 0:
            return max(max_sum, total_sum)
        else:
            return max(max_sum, prefix_sum + suffix_sum)
      
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kConcatenationMaxSum(arr, k)
    print("\noutput:", serialize(ans, "integer"))
