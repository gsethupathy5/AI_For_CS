# Created by asetti2002 at 2024/04/25 19:42
# leetgo: 1.4.3
# https://leetcode.com/problems/reorder-data-in-log-files/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digitz_logs = []
        
        for log in logs:
            if log.split()[1].isdigit():
                digitz_logs.append(log)
            else:
                letter_logs.append(log)
        
        letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))
   	    return letter_logs + digitz_logs

# @lc code=end

if __name__ == "__main__":
    logs: List[str] = deserialize("List[str]", read_line())
    ans = Solution().reorderLogFiles(logs)
    print("\noutput:", serialize(ans, "string[]"))
