# Created by asetti2002 at 2024/04/25 19:47
# leetgo: 1.4.3
# https://leetcode.com/problems/vowel-spellchecker/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def replace_vowels(word):
            vowels = 'aeiou'
            res = []
            for char in word:
                res.append('#' if char.lower() in vowels else char.lower())
            return ''.join(res)

        words_set = set(wordlist)
        words_dict = {}
        for word in wordlist:
            lower_word = word.lower()
            words_dict.setdefault(lower_word, word)
            words_dict.setdefault(replace_vowels(lower_word), word)

        def check_word(word):
            lower_word = word.lower()
            if word in words_set:
                return word
            if lower_word in words_dict:
                return words_dict[lower_word]
            replaced = replace_vowels(lower_word)
            if replaced in words_dict:
                return words_dict[replaced]
            return ""
        
        return [check_word(query) for query in queries]
# @lc code=end

if __name__ == "__main__":
    wordlist: List[str] = deserialize("List[str]", read_line())
    queries: List[str] = deserialize("List[str]", read_line())
    ans = Solution().spellchecker(wordlist, queries)
    print("\noutput:", serialize(ans, "string[]"))
