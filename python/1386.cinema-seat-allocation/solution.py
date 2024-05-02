# Created by asetti2002 at 2024/04/25 20:35
# leetgo: 1.4.3
# https://leetcode.com/problems/cinema-seat-allocation/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved = collections.defaultdict(set)
        for seat in reservedSeats:
            row, seat_num = seat
            reserved[row].add(seat_num)
        
        result = 2 * n
        count = 0
        
        for row in reserved:
            if not reserved[row] & {2, 3, 4, 5} and not reserved[row] & {6, 7, 8, 9} and not reserved[row] & {4, 5, 6, 7}:
                count += 2
            elif not reserved[row] & {2, 3, 4, 5} or not reserved[row] & {6, 7, 8, 9} or not reserved[row] & {4, 5, 6, 7}:
                count += 1
        
        return result + count
# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    reservedSeats: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().maxNumberOfFamilies(n, reservedSeats)
    print("\noutput:", serialize(ans, "integer"))
