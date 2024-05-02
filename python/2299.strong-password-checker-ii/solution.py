# Created by asetti2002 at 2024/05/01 19:45
# leetgo: 1.4.3
# https://leetcode.com/problems/strong-password-checker-ii/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        return len(password) >= 8 and any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password) and any(c in "!@#$%^&*()-+" for c in password) and not any(password[i] == password[i+1] for i in range(len(password) - 1))
# @lc code=end

if __name__ == "__main__":
    password: str = deserialize("str", read_line())
    ans = Solution().strongPasswordCheckerII(password)
    print("\noutput:", serialize(ans, "boolean"))
