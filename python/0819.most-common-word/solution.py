# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/most-common-word/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        

# @lc code=end

if __name__ == "__main__":
    paragraph: str = deserialize("str", read_line())
    banned: List[str] = deserialize("List[str]", read_line())
    ans = Solution().mostCommonWord(paragraph, banned)
    print("\noutput:", serialize(ans, "string"))
