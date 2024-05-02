# Created by asetti2002 at 2024/04/25 20:02
# leetgo: 1.4.3
# https://leetcode.com/problems/corporate-flight-bookings/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0] * n
        for booking in bookings:
            first, last, seats = booking
            ans[first - 1] += seats
            if last < n:
                ans[last] -= seats

        for i in range(1, n):
            ans[i] += ans[i - 1]

        return ans
# @lc code=end

if __name__ == "__main__":
    bookings: List[List[int]] = deserialize("List[List[int]]", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().corpFlightBookings(bookings, n)
    print("\noutput:", serialize(ans, "integer[]"))
