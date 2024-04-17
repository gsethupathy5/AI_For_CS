# [2223. Sum of Scores of Built Strings][link] (Hard)

[link]: https://leetcode.com/problems/sum-of-scores-of-built-strings/

You are **building** a string `s` of length `n` **one** character at a time, **prepending** each new
character to the **front** of the string. The strings are labeled from `1` to `n`, where the string
with length `i` is labeled `sᵢ`.

- For example, for `s = "abaca"`, `s₁ == "a"`, `s₂ == "ca"`, `s₃ == "aca"`, etc.

The **score** of `sᵢ` is the length of the **longest common prefix** between `sᵢ` and `sₙ` (Note
that `s == sₙ`).

Given the final string `s`, return the **sum** of the **score** of every  `sᵢ`.

**Example 1:**

```
Input: s = "babab"
Output: 9
Explanation:
For s₁ == "b", the longest common prefix is "b" which has a score of 1.
For s₂ == "ab", there is no common prefix so the score is 0.
For s₃ == "bab", the longest common prefix is "bab" which has a score of 3.
For s₄ == "abab", there is no common prefix so the score is 0.
For s₅ == "babab", the longest common prefix is "babab" which has a score of 5.
The sum of the scores is 1 + 0 + 3 + 0 + 5 = 9, so we return 9.
```

**Example 2:**

```
Input: s = "azbazbzaz"
Output: 14
Explanation:
For s₂ == "az", the longest common prefix is "az" which has a score of 2.
For s₆ == "azbzaz", the longest common prefix is "azb" which has a score of 3.
For s₉ == "azbazbzaz", the longest common prefix is "azbazbzaz" which has a score of 9.
For all other sᵢ, the score is 0.
The sum of the scores is 2 + 3 + 9 = 14, so we return 14.
```

**Constraints:**

- `1 <= s.length <= 10⁵`
- `s` consists of lowercase English letters.
