# Created by asetti2002 at 2024/04/25 20:06
# leetgo: 1.4.3
# https://leetcode.com/problems/decompress-run-length-encoded-list/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums), 2):
            result.extend([nums[i+1]] * nums[i])
        return result
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().decompressRLElist(nums)
    print("\noutput:", serialize(ans, "integer[]"))
