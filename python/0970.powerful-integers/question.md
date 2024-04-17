# [970. Powerful Integers][link] (Medium)

[link]: https://leetcode.com/problems/powerful-integers/

Given three integers `x`, `y`, and `bound`, return a list of all the **powerful integers** that have
a value less than or equal to `bound`.

An integer is **powerful** if it can be represented as `xⁱ + yʲ` for some integers `i >= 0` and `j
>= 0`.

You may return the answer in **any order**. In your answer, each value should occur **at most
once**.

**Example 1:**

```
Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation:
2 = 2⁰ + 3⁰
3 = 2¹ + 3⁰
4 = 2⁰ + 3¹
5 = 2¹ + 3¹
7 = 2² + 3¹
9 = 2³ + 3⁰
10 = 2⁰ + 3²
```

**Example 2:**

```
Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]
```

**Constraints:**

- `1 <= x, y <= 100`
- `0 <= bound <= 10⁶`
