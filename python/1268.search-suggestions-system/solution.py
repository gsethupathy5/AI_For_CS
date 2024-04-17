# Created by asetti2002 at 2024/04/17 02:12
# leetgo: 1.4.3
# https://leetcode.com/problems/search-suggestions-system/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        

# @lc code=end

if __name__ == "__main__":
    products: List[str] = deserialize("List[str]", read_line())
    searchWord: str = deserialize("str", read_line())
    ans = Solution().suggestedProducts(products, searchWord)
    print("\noutput:", serialize(ans, "string[][]"))
