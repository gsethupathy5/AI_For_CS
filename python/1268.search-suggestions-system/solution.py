# Created by asetti2002 at 2024/04/25 20:25
# leetgo: 1.4.3
# https://leetcode.com/problems/search-suggestions-system/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        import bisect
        products.sort()
        res = []
        prefix = ""
        for char in searchWord:
            prefix += char
            i = bisect.bisect_left(products, prefix)
            res.append([product for product in products[i:i+3] if product.startswith(prefix)])
        return res
# @lc code=end

if __name__ == "__main__":
    products: List[str] = deserialize("List[str]", read_line())
    searchWord: str = deserialize("str", read_line())
    ans = Solution().suggestedProducts(products, searchWord)
    print("\noutput:", serialize(ans, "string[][]"))
