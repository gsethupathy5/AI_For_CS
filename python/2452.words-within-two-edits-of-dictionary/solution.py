# Created by asetti2002 at 2024/05/01 20:03
# leetgo: 1.4.3
# https://leetcode.com/problems/words-within-two-edits-of-dictionary/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def is_edit_distance_one(word1, word2):
            if len(word1) != len(word2):
                return False
            count_diff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    count_diff += 1
                if count_diff > 1:
                    return False
            return count_diff == 1

        def is_edit_distance_two(word1, word2):
            if len(word1) != len(word2):
                return False
            count_diff = 0
            for i in range(len(word1)):
                if word1[i] != word2[i]:
                    count_diff += 1
                if count_diff > 2:
                    return False
            return count_diff == 2

        result = []
        for query in queries:
            match_found = False
            if query in dictionary:
                result.append(query)
                match_found = True
            else:
                for word in dictionary:
                    if is_edit_distance_one(query, word) or is_edit_distance_two(query, word):
                        result.append(query)
                        match_found = True
                        break
            if not match_found:
                result = result

        return result
# @lc code=end

if __name__ == "__main__":
    queries: List[str] = deserialize("List[str]", read_line())
    dictionary: List[str] = deserialize("List[str]", read_line())
    ans = Solution().twoEditWords(queries, dictionary)
    print("\noutput:", serialize(ans, "string[]"))
