# Created by asetti2002 at 2024/05/01 20:09
# leetgo: 1.4.3
# https://leetcode.com/problems/reward-top-k-students/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        feedback_dict = {}
        for i in range(len(student_id)):
            points = 0
            feedback = report[i].split()
            for word in feedback:
                if word in positive_feedback:
                    points += 3
                elif word in negative_feedback:
                    points -= 1
            if student_id[i] not in feedback_dict:
                feedback_dict[student_id[i]] = points
            else:
                feedback_dict[student_id[i]] += points
        
        sorted_students = sorted(feedback_dict.items(), key=lambda x: (x[1], -x[0]), reverse=True)
        
        top_k_students = [student[0] for student in sorted_students[:k]]
        
        return top_k_students
# @lc code=end

if __name__ == "__main__":
    positive_feedback: List[str] = deserialize("List[str]", read_line())
    negative_feedback: List[str] = deserialize("List[str]", read_line())
    report: List[str] = deserialize("List[str]", read_line())
    student_id: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().topStudents(positive_feedback, negative_feedback, report, student_id, k)
    print("\noutput:", serialize(ans, "integer[]"))
