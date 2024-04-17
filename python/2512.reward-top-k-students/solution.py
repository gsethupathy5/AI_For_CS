# Created by asetti2002 at 2024/04/17 02:04
# leetgo: 1.4.3
# https://leetcode.com/problems/reward-top-k-students/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        

# @lc code=end

if __name__ == "__main__":
    positive_feedback: List[str] = deserialize("List[str]", read_line())
    negative_feedback: List[str] = deserialize("List[str]", read_line())
    report: List[str] = deserialize("List[str]", read_line())
    student_id: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().topStudents(positive_feedback, negative_feedback, report, student_id, k)
    print("\noutput:", serialize(ans, "integer[]"))
