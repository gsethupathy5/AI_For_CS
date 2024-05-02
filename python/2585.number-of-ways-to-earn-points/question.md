# [2585. Number of Ways to Earn Points][link] (Hard)

[link]: https://leetcode.com/problems/number-of-ways-to-earn-points/

There is a test that has `n` types of questions. You are given an integer `target` and a **0-
indexed** 2D integer array `types` where `types[i] = [countᵢ, marksᵢ]` indicates that there are
`countᵢ` questions of the `iᵗʰ` type, and each one of them is worth `marksᵢ` points.

Return the number of ways you can earn **exactly** `target` points in the exam. Since the answer may
be too large, return it **modulo** `10⁹ + 7`.

**Note** that questions of the same type are indistinguishable.

- For example, if there are `3` questions of the same type, then solving the `1ˢᵗ` and `2ⁿᵈ`
questions is the same as solving the `1ˢᵗ` and `3ʳᵈ` questions, or the `2ⁿᵈ` and `3ʳᵈ` questions.

**Example 1:**

```
Input: target = 6, types = [[6,1],[3,2],[2,3]]
Output: 7
Explanation: You can earn 6 points in one of the seven ways:
- Solve 6 questions of the 0ᵗʰ type: 1 + 1 + 1 + 1 + 1 + 1 = 6
- Solve 4 questions of the 0ᵗʰ type and 1 question of the 1ˢᵗ type: 1 + 1 + 1 + 1 + 2 = 6
- Solve 2 questions of the 0ᵗʰ type and 2 questions of the 1ˢᵗ type: 1 + 1 + 2 + 2 = 6
- Solve 3 questions of the 0ᵗʰ type and 1 question of the 2ⁿᵈ type: 1 + 1 + 1 + 3 = 6
- Solve 1 question of the 0ᵗʰ type, 1 question of the 1ˢᵗ type and 1 question of the 2ⁿᵈ type: 1 + 2
+ 3 = 6
- Solve 3 questions of the 1ˢᵗ type: 2 + 2 + 2 = 6
- Solve 2 questions of the 2ⁿᵈ type: 3 + 3 = 6
```

**Example 2:**

```
Input: target = 5, types = [[50,1],[50,2],[50,5]]
Output: 4
Explanation: You can earn 5 points in one of the four ways:
- Solve 5 questions of the 0ᵗʰ type: 1 + 1 + 1 + 1 + 1 = 5
- Solve 3 questions of the 0ᵗʰ type and 1 question of the 1ˢᵗ type: 1 + 1 + 1 + 2 = 5
- Solve 1 questions of the 0ᵗʰ type and 2 questions of the 1ˢᵗ type: 1 + 2 + 2 = 5
- Solve 1 question of the 2ⁿᵈ type: 5
```

**Example 3:**

```
Input: target = 18, types = [[6,1],[3,2],[2,3]]
Output: 1
Explanation: You can only earn 18 points by answering all questions.
```

**Constraints:**

- `1 <= target <= 1000`
- `n == types.length`
- `1 <= n <= 50`
- `types[i].length == 2`
- `1 <= countᵢ, marksᵢ <= 50`
