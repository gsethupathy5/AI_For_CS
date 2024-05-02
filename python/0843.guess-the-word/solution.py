# Created by asetti2002 at 2024/04/25 19:29
# leetgo: 1.4.3
# https://leetcode.com/problems/guess-the-word/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def guess(self, word: str) -> int:
        def get_score(w1, w2):
            score = 0
            for c1, c2 in zip(w1, w2):
                if c1 == c2:
                    score += 1
            return score
        
        def findSecretWord(words, master):
            n = len(words)
            guesses = 0
            
            while guesses < 10:
                guess_word = words[0]
                score = master.guess(guess_word)
                
                if score == 6:
                    return
                
                new_words = []
                for word in words:
                    if get_score(guess_word, word) == score:
                        new_words.append(word)
                
                words = new_words
                guesses += 1
        
        findSecretWord(words, master)
# @lc code=end

# Warning: this is a manual question, the generated test code may be incorrect.
if __name__ == "__main__":
    secret: str = deserialize("str", read_line())
    words: List[str] = deserialize("List[str]", read_line())
    allowedGuesses: int = deserialize("int", read_line())
    findSecretWord(secret, words, allowedGuesses)
    ans = None
    print("\noutput:", "null")
