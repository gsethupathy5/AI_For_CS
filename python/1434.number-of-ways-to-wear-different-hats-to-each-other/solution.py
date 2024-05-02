# Created by asetti2002 at 2024/04/25 20:41
# leetgo: 1.4.3
# https://leetcode.com/problems/number-of-ways-to-wear-different-hats-to-each-other/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(hats)
        all_hats = (1 << 40) - 1
        dp = [0] * (1 << 40)
        dp[0] = 1

        for i in range(1, 41):
            people_with_hat = defaultdict(int)
            for person, hats_list in enumerate(hats):
                for hat in hats_list:
                    people_with_hat[hat] |= (1 << person)

            new_dp = dp[:]
            for state in range(all_hats, -1, -1):
                for person in range(n):
                    if people_with_hat.get(i, 0) & (1 << person):
                        new_dp[state | (1 << i)] += dp[state]
                        new_dp[state | (1 << i)] %= MOD
            dp = new_dp
        
        return dp[all_hats]


# Note: Make sure to import the necessary libraries (e.g. List, defaultdict) at the beginning of the script.
# @lc code=end

if __name__ == "__main__":
    hats: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().numberWays(hats)
    print("\noutput:", serialize(ans, "integer"))
