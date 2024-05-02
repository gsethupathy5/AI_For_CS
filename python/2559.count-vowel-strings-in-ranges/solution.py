# Created by asetti2002 at 2024/05/01 20:18
# leetgo: 1.4.3
# https://leetcode.com/problems/count-vowel-strings-in-ranges/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def count_vowel(word):
            count = 0
            vowels = ['a', 'e', 'i', 'o', 'u']
            for char in word:
                if char in vowels:
                    count += 1
            return count
        
        ans = []
        for query in queries:
            start, end = query
            count = 0
            for i in range(start, end+1):
                if count_vowel(words[i][0]) > 0 and count_vowel(words[i][-1]) > 0:
                    count += 1
            ans.append(count)
        
        return ans
# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    queries: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().vowelStrings(words, queries)
    print("\noutput:", serialize(ans, "integer[]"))
