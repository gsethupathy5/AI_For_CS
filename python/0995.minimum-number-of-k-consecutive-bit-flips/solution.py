# Created by asetti2002 at 2024/04/25 19:51
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip_count = 0
        flipped = [False] * n
        total_flips = 0
        
        for i in range(n):
            if i >= k:
                flip_count -= flipped[i - k]
                
            if (nums[i] + flip_count) % 2 == 0:
                if i + k > n:
                    return -1
                flip_count += 1
                total_flips += 1
                flipped[i] = True
                
        return total_flips
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minKBitFlips(nums, k)
    print("\noutput:", serialize(ans, "integer"))
