# Created by asetti2002 at 2024/05/01 20:09
# leetgo: 1.4.3
# https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        def get_distance(word1, word2, n):
            return min(abs(words.index(word1) - words.index(word2)), n - abs(words.index(word1) - words.index(word2))
        
        n = len(words)
        if target not in words:
            return -1
        
        min_distance = float('inf')
        for i in range(n):
            if words[i] == target:
                min_distance = min(min_distance, get_distance(words[startIndex], target, n))
        
        return min_distance
# @lc code=end

if __name__ == "__main__":
    words: List[str] = deserialize("List[str]", read_line())
    target: str = deserialize("str", read_line())
    startIndex: int = deserialize("int", read_line())
    ans = Solution().closetTarget(words, target, startIndex)
    print("\noutput:", serialize(ans, "integer"))
