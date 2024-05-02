# Created by asetti2002 at 2024/04/25 19:33
# leetgo: 1.4.3
# https://leetcode.com/problems/advantage-shuffle/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        import bisect
        
        nums1.sort()
        nums2_sorted = sorted(nums2)
        result = []
        no_match = []
        
        for num in nums2:
            i = bisect.bisect_right(nums1, num)
            if i == len(nums1):
                no_match.append(num)
            else:
                result.append(nums1[i])
                nums1.pop(i)
        
        return result + no_match
# @lc code=end

if __name__ == "__main__":
    nums1: List[int] = deserialize("List[int]", read_line())
    nums2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().advantageCount(nums1, nums2)
    print("\noutput:", serialize(ans, "integer[]"))
