# Created by asetti2002 at 2024/04/25 20:02
# leetgo: 1.4.3
# https://leetcode.com/problems/filling-bookcase-shelves/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [0] + [float('inf')] * n
        
        for i in range(1, n + 1):
            width = height = 0
            j = i - 1
            while j >= 0 and width + books[j][0] <= shelfWidth:
                width += books[j][0]
                height = max(height, books[j][1])
                dp[i] = min(dp[i], dp[j] + height)
                j -= 1
        
        return dp[n]
# @lc code=end

if __name__ == "__main__":
    books: List[List[int]] = deserialize("List[List[int]]", read_line())
    shelfWidth: int = deserialize("int", read_line())
    ans = Solution().minHeightShelves(books, shelfWidth)
    print("\noutput:", serialize(ans, "integer"))
