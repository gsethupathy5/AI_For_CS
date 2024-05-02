# Created by asetti2002 at 2024/04/25 19:41
# leetgo: 1.4.3
# https://leetcode.com/problems/unique-email-addresses/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = local_name.split('+')[0].replace('.', '')
            unique_emails.add(local_name + '@' + domain_name)
        return len(unique_emails)
# @lc code=end

if __name__ == "__main__":
    emails: List[str] = deserialize("List[str]", read_line())
    ans = Solution().numUniqueEmails(emails)
    print("\noutput:", serialize(ans, "integer"))
