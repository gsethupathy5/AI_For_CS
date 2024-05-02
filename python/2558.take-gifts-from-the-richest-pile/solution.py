# Created by asetti2002 at 2024/05/01 20:18
# leetgo: 1.4.3
# https://leetcode.com/problems/take-gifts-from-the-richest-pile/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        return sum([max(0, gift - int(gift ** 0.5)) for gift in gifts]) - k * len(gifts)
# @lc code=end

if __name__ == "__main__":
    gifts: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().pickGifts(gifts, k)
    print("\noutput:", serialize(ans, "long"))
