# Created by asetti2002 at 2024/04/25 19:40
# leetgo: 1.4.3
# https://leetcode.com/problems/sort-array-by-parity-ii/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = 0
        odd = 1
        sorted_arr = [0] * len(nums)
        
        for num in nums:
            if num % 2 == 0:
                sorted_arr[even] = num
                even += 2
            else:
                sorted_arr[odd] = num
                odd += 2
                
        return sorted_arr
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sortArrayByParityII(nums)
    print("\noutput:", serialize(ans, "integer[]"))
