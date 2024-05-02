# Created by asetti2002 at 2024/05/01 20:01
# leetgo: 1.4.3
# https://leetcode.com/problems/remove-letter-to-equalize-frequency/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def equalFrequency(self, word: str) -> bool:
        def check_freq(word):
            freq = {}
            for letter in word:
                if letter in freq:
                    freq[letter] += 1
                else:
                    freq[letter] = 1
            return list(freq.values())
        
        frequencies = check_freq(word)
        unique_freq = set(frequencies)
        
        if len(unique_freq) == 1:
            return True
        
        if len(unique_freq) > 2:
            return False
        
        for freq in unique_freq:
            if frequencies.count(freq) == 1:
                return True if 1 in frequencies or abs(frequencies[0]-frequencies[1]) == 1 else False
        
        return False
# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    ans = Solution().equalFrequency(word)
    print("\noutput:", serialize(ans, "boolean"))
