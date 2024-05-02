# Created by asetti2002 at 2024/04/25 19:25
# leetgo: 1.4.3
# https://leetcode.com/problems/goat-latin/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set('aeiouAEIOU')
        words = sentence.split()
        
        result = []
        for i, word in enumerate(words):
            if word[0] in vowels:
                result.append(word + 'ma' + 'a'*(i+1))
            else:
                result.append(word[1:] + word[0] + 'ma' + 'a'*(i+1))
        
        return ' '.join(result)
# @lc code=end

if __name__ == "__main__":
    sentence: str = deserialize("str", read_line())
    ans = Solution().toGoatLatin(sentence)
    print("\noutput:", serialize(ans, "string"))
