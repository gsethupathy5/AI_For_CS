# Created by asetti2002 at 2024/04/17 02:16
# leetgo: 1.4.3
# https://leetcode.com/problems/replace-words/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        

# @lc code=end

if __name__ == "__main__":
    dictionary: List[str] = deserialize("List[str]", read_line())
    sentence: str = deserialize("str", read_line())
    ans = Solution().replaceWords(dictionary, sentence)
    print("\noutput:", serialize(ans, "string"))
