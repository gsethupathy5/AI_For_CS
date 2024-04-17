# Created by asetti2002 at 2024/04/17 02:14
# leetgo: 1.4.3
# https://leetcode.com/problems/vowel-spellchecker/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        

# @lc code=end

if __name__ == "__main__":
    wordlist: List[str] = deserialize("List[str]", read_line())
    queries: List[str] = deserialize("List[str]", read_line())
    ans = Solution().spellchecker(wordlist, queries)
    print("\noutput:", serialize(ans, "string[]"))
