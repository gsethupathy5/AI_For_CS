# Created by asetti2002 at 2024/05/01 20:14
# leetgo: 1.4.3
# https://leetcode.com/problems/separate-the-digits-in-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            for digit in str(num):
                answer.append(int(digit))
        return answer
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().separateDigits(nums)
    print("\noutput:", serialize(ans, "integer[]"))
