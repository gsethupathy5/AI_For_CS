# Created by asetti2002 at 2024/05/01 19:43
# leetgo: 1.4.3
# https://leetcode.com/problems/apply-discount-to-prices/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        import re

        def apply_discount(match):
            price = float(match.group(0)[1:])
            discounted_price = price * (1 - discount / 100)
            return f"${discounted_price:.2f}"
        
        return re.sub(r'\$\d+\.?\d*', apply_discount, sentence)
# @lc code=end

if __name__ == "__main__":
    sentence: str = deserialize("str", read_line())
    discount: int = deserialize("int", read_line())
    ans = Solution().discountPrices(sentence, discount)
    print("\noutput:", serialize(ans, "string"))
