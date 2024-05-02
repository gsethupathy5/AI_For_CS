# Created by asetti2002 at 2024/04/25 19:44
# leetgo: 1.4.3
# https://leetcode.com/problems/bag-of-tokens/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score = 0
        max_score = 0
        left = 0
        right = len(tokens) - 1
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
        return max_score
# @lc code=end

if __name__ == "__main__":
    tokens: List[int] = deserialize("List[int]", read_line())
    power: int = deserialize("int", read_line())
    ans = Solution().bagOfTokensScore(tokens, power)
    print("\noutput:", serialize(ans, "integer"))
