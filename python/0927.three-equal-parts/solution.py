# Created by asetti2002 at 2024/04/25 19:41
# leetgo: 1.4.3
# https://leetcode.com/problems/three-equal-parts/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        def find_trailing_zeros(arr):
            count = 0
            for i in range(len(arr) - 1, -1, -1):
                if arr[i] == 0:
                    count += 1
                else:
                    break
            return count
        
        total_ones = sum(arr)
        
        if total_ones % 3 != 0:
            return [-1, -1]
        
        if total_ones == 0:
            return [0, len(arr) - 1]
        
        ones_per_part = total_ones // 3
        
        end_zeros_count = find_trailing_zeros(arr)
        
        i = 0
        ones_count = 0
        while ones_count < ones_per_part:
            ones_count += arr[i]
            i += 1
        
        j = i
        ones_count = 0
        while ones_count < ones_per_part:
            ones_count += arr[j]
            j += 1
        
        k = j
        ones_count = 0
        while ones_count < ones_per_part:
            ones_count += arr[k]
            k += 1
        
        while k < len(arr) and arr[i] == arr[j] == arr[k]:
            i += 1
            j += 1
            k += 1
        
        if k == len(arr):
            return [i - 1 + end_zeros_count, j + end_zeros_count]
        else:
            return [-1, -1]
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().threeEqualParts(arr)
    print("\noutput:", serialize(ans, "integer[]"))
