# Created by asetti2002 at 2024/04/25 19:27
# leetgo: 1.4.3
# https://leetcode.com/problems/masking-personal-information/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            name, domain = s.lower().split('@')
            return '{}*****{}@{}'.format(name[0], name[-1], domain)
        else:
            digits = ''.join(filter(str.isdigit, s))
            local = '***-***-{}'.format(digits[-4:])
            if len(digits) == 10:
                return local
            return '+{}-'.format('*'*(len(digits)-10)) + local
# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().maskPII(s)
    print("\noutput:", serialize(ans, "string"))
