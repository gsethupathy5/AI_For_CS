# Created by asetti2002 at 2024/04/25 20:04
# leetgo: 1.4.3
# https://leetcode.com/problems/smallest-sufficient-team/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        def backtrack(people_skills, skill_idx, total_skills):
            if skill_idx == len(req_skills):
                return []

            if skill_idx in total_skills:
                return total_skills[skill_idx]

            best_team = None
            for i, person_skills in enumerate(people_skills):
                if req_skills[skill_idx] in person_skills:
                    new_skills = total_skills.copy()
                    new_skills[skill_idx] = [i]
                    updated_team = backtrack(people_skills, skill_idx + 1, new_skills)
                    if updated_team is None:
                        continue
                    updated_team = [i] + updated_team
                    if best_team is None or len(updated_team) < len(best_team):
                        best_team = updated_team

            total_skills[skill_idx] = best_team
            return best_team

        people_skills = [set(skills) for skills in people]
        total_skills = {}
        result = backtrack(people_skills, 0, total_skills)
        return result if result is not None else []
# @lc code=end

if __name__ == "__main__":
    req_skills: List[str] = deserialize("List[str]", read_line())
    people: List[List[str]] = deserialize("List[List[str]]", read_line())
    ans = Solution().smallestSufficientTeam(req_skills, people)
    print("\noutput:", serialize(ans, "integer[]"))
