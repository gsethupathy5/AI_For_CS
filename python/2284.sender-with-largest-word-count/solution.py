# Created by asetti2002 at 2024/05/01 19:43
# leetgo: 1.4.3
# https://leetcode.com/problems/sender-with-largest-word-count/

from typing import *
from leetgo_py import *

# @lc code=begin
class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        sender_word_count = {}
        for i in range(len(messages)):
            sender = senders[i]
            words = messages[i].split()
            if sender in sender_word_count:
                sender_word_count[sender] += len(words)
            else:
                sender_word_count[sender] = len(words)

        max_word_count = max(sender_word_count.values())
        max_senders = [sender for sender, count in sender_word_count.items() if count == max_word_count]
        return max(max_senders)
# @lc code=end

if __name__ == "__main__":
    messages: List[str] = deserialize("List[str]", read_line())
    senders: List[str] = deserialize("List[str]", read_line())
    ans = Solution().largestWordCount(messages, senders)
    print("\noutput:", serialize(ans, "string"))
