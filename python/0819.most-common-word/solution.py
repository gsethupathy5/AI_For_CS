# Created by asetti2002 at 2024/04/25 19:07
# leetgo: 1.4.3
# https://leetcode.com/problems/most-common-word/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re
        from collections import Counter
        
        words = re.findall(r'\w+', paragraph.lower())
        words = [word for word in words if word not in set(banned)]
        
        word_freq = Counter(words)
        
        max_freq_word, _ = max(word_freq.items(), key=lambda x: x[1])
        
        return max_freq_word
# @lc code=end

if __name__ == "__main__":
    paragraph: str = deserialize("str", read_line())
    banned: List[str] = deserialize("List[str]", read_line())
    ans = Solution().mostCommonWord(paragraph, banned)
    print("\noutput:", serialize(ans, "string"))
