# Created by asetti2002 at 2024/05/01 19:56
# leetgo: 1.4.3
# https://leetcode.com/problems/most-frequent-even-element/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num % 2 == 0:
                count[num] = count.get(num, 0) + 1
        
        max_freq = 0
        most_frequent_even = -1
        for num, freq in count.items():
            if freq > max_freq or (freq == max_freq and num < most_frequent_even):
                max_freq = freq
                most_frequent_even = num
        
        return most_frequent_even
# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().mostFrequentEven(nums)
    print("\noutput:", serialize(ans, "integer"))
