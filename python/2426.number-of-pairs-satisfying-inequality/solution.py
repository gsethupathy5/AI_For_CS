# Created by asetti2002 at 2024/05/01 19:59
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        count = 0
        for i in range(len(nums1)):
            for j in range(i+1, len(nums1)):
                if nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff:
                    count += 1
        return count
# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    diff: int = deserialize("int", read_line())
    ans = Solution().numberOfPairs(nums1, nums2, diff)
    print("\noutput:", serialize(ans, "long"))
