# Created by asetti2002 at 2024/04/17 02:06
# leetgo: 1.4.3
# https://leetcode.com/problems/apply-discount-to-prices/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        

# @lc code=end

if __name__ == "__main__":
    sentence: str = deserialize("str", read_line())
    discount: int = deserialize("int", read_line())
    ans = Solution().discountPrices(sentence, discount)
    print("\noutput:", serialize(ans, "string"))
