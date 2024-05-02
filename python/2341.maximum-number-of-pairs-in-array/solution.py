# Created by asetti2002 at 2024/05/01 19:48
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-number-of-pairs-in-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counts = {}
        pairs = 0
        
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        for num in counts.values():
            pairs += num // 2
        
        leftover = sum(num % 2 for num in counts.values())
        
        return [pairs, leftover]
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().numberOfPairs(nums)
    print("\noutput:", serialize(ans, "integer[]"))
