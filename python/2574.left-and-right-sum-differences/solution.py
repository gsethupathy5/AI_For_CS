# Created by asetti2002 at 2024/05/01 20:21
# leetgo: 1.4.3
# https://leetcode.com/problems/left-and-right-sum-differences/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n
        answer = [0] * n
        
        leftSum[0] = 0
        rightSum[n-1] = 0
        
        for i in range(1, n):
            leftSum[i] = leftSum[i-1] + nums[i-1]
        
        for i in range(n-2, -1, -1):
            rightSum[i] = rightSum[i+1] + nums[i+1]
        
        for i in range(n):
            answer[i] = abs(leftSum[i] - rightSum[i])
        
        return answer
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().leftRightDifference(nums)
    print("\noutput:", serialize(ans, "integer[]"))
