# Created by asetti2002 at 2024/05/01 20:12
# leetgo: 1.4.3
# https://leetcode.com/problems/count-the-number-of-good-subarrays/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + (num % 2 == 1))
        cnt = {}
        for x in prefix:
            count += cnt.get(x - k, 0)
            cnt[x] = cnt.get(x, 0) + 1
        return count
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().countGood(nums, k)
    print("\noutput:", serialize(ans, "long"))
