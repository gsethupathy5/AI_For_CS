# Created by asetti2002 at 2024/05/01 19:53
# leetgo: 1.4.3
# https://leetcode.com/problems/maximum-segment-sum-after-removals/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        seg_sum = [0] * (n + 1)
        max_seg_sum = [0] * (n + 1)
        
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]
        
        for i in range(n):
            seg_sum[i] = prefix_sum[i+1] - prefix_sum[removeQueries[i]+1]
        
        s = []
        for i in range(n):
            while s and s[-1] < seg_sum[i]:
                s.pop()
            if s:
                max_seg_sum[i] = max(s[-1], 0)
            s.append(seg_sum[i])
        
        answer = []
        for i in range(n-1, -1, -1):
            answer.append(max_seg_sum[i])
            if max_seg_sum[i] == seg_sum[i]:
                s.pop()
            while s and s[-1] < seg_sum[i]:
                s.pop()
            if s:
                max_seg_sum[i] = max(s[-1], 0)
            s.append(seg_sum[i])
        
        return answer[::-1]
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    removeQueries: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumSegmentSum(nums, removeQueries)
    print("\noutput:", serialize(ans, "long[]"))
