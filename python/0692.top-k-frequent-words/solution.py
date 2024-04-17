# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/top-k-frequent-words/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().topKFrequent(words, k)
    print("\noutput:", serialize(ans, "string[]"))
