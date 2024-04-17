# Created by asetti2002 at 2024/04/17 02:15
# leetgo: 1.4.3
# https://leetcode.com/problems/guess-the-word/

from typing import *
from leetgo_py import *

# @lc code=begin

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        

# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    secret: str = deserialize("str", read_line())
    words: List[str] = deserialize("List[str]", read_line())
    allowedGuesses: int = deserialize("int", read_line())
    findSecretWord(secret, words, allowedGuesses)
    ans = None
    print("\noutput:", "null")
