# Created by asetti2002 at 2024/04/25 20:15
# leetgo: 1.4.3
# https://leetcode.com/problems/unique-number-of-occurrences/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)
        return len(count.values()) == len(set(count.values()))
# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().uniqueOccurrences(arr)
    print("\noutput:", serialize(ans, "boolean"))
