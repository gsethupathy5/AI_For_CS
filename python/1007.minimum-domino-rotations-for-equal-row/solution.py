# Created by asetti2002 at 2024/04/25 19:52
# leetgo: 1.4.3
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        from collections import Counter
        
        if len(tops) != len(bottoms):
            return -1
        
        n = len(tops)
        freq_tops = Counter(tops)
        freq_bottoms = Counter(bottoms)
        freq_same = Counter()
        
        for i in range(n):
            if tops[i] == bottoms[i]:
                freq_same[tops[i]] += 1
        
        min_swaps = float('inf')
        for num in range(1, 7):
            if freq_tops[num] + freq_bottoms[num] - freq_same[num] == n:
                min_swaps = min(min_swaps, n - max(freq_tops[num], freq_bottoms[num]))
        
        return min_swaps if min_swaps != float('inf') else -1
# @lc code=end

if __name__ == "__main__":
    tops: List[int] = deserialize("List[int]", read_line())
    bottoms: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minDominoRotations(tops, bottoms)
    print("\noutput:", serialize(ans, "integer"))
