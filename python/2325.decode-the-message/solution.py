# Created by asetti2002 at 2024/05/01 19:47
# leetgo: 1.4.3
# https://leetcode.com/problems/decode-the-message/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        import string
        
        table = {}
        for i, char in enumerate(key):
            if char != ' ' and char not in table:
                table[char] = string.ascii_lowercase[i]
        
        decoded_message = ''
        for char in message:
            if char == ' ':
                decoded_message += ' '
            else:
                decoded_message += table[char]
        
        return decoded_message
# @lc code=end

if __name__ == "__main__":
    key: str = deserialize("str", read_line())
    message: str = deserialize("str", read_line())
    ans = Solution().decodeMessage(key, message)
    print("\noutput:", serialize(ans, "string"))
