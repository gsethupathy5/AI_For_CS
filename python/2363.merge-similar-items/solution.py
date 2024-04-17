# Created by asetti2002 at 2024/04/17 02:05
# leetgo: 1.4.3
# https://leetcode.com/problems/merge-similar-items/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        

# @lc code=end

if __name__ == "__main__":
    items1: List[List[int]] = deserialize("List[List[int]]", read_line())
    items2: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().mergeSimilarItems(items1, items2)
    print("\noutput:", serialize(ans, "integer[][]"))
