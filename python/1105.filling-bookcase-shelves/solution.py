# Created by asetti2002 at 2024/04/17 02:13
# leetgo: 1.4.3
# https://leetcode.com/problems/filling-bookcase-shelves/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        

# @lc code=end

if __name__ == "__main__":
    books: List[List[int]] = deserialize("List[List[int]]", read_line())
    shelfWidth: int = deserialize("int", read_line())
    ans = Solution().minHeightShelves(books, shelfWidth)
    print("\noutput:", serialize(ans, "integer"))
