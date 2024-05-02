# Created by asetti2002 at 2024/04/25 20:02
# leetgo: 1.4.3
# https://leetcode.com/problems/find-in-mountain-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def get(self, index: int) -> int:
        def find_peak(left, right):
            while left < right:
                mid = (left + right) // 2
                if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                    left = mid + 1
                else:
                    right = mid
            return left
        
        def binary_search(left, right, target, increasing):
            while left <= right:
                mid = (left + right) // 2
                if target == mountain_arr.get(mid):
                    return mid
                if increasing:
                    if target < mountain_arr.get(mid):
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if target > mountain_arr.get(mid):
                        right = mid - 1
                    else:
                        left = mid + 1
            return -1
        
        n = mountain_arr.length()
        left, right = 0, n - 1
        peak_index = find_peak(left, right)
        
        result = binary_search(left, peak_index, target, True)
        if result != -1:
            return result
        
        return binary_search(peak_index, right, target, False)
# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    secret: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().findInMountainArray(secret, target)
    print("\noutput:", serialize(ans, "integer"))
