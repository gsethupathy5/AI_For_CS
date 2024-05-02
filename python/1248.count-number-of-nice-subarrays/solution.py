# Created by asetti2002 at 2024/04/25 20:22
# leetgo: 1.4.3
# https://leetcode.com/problems/count-number-of-nice-subarrays/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        map = {0: 1}
        odd_count = 0
        
        for num in nums:
            if num % 2 == 1:
                odd_count += 1
            
            if odd_count - k in map:
                count += map[odd_count - k]
            
            map[odd_count] = map.get(odd_count, 0) + 1
        
        return count
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().numberOfSubarrays(nums, k)
    print("\noutput:", serialize(ans, "integer"))
