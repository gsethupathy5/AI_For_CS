# [2155. All Divisions With the Highest Score of a Binary Array][link] (Medium)

[link]: https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

You are given a **0-indexed** binary array `nums` of length `n`. `nums` can be divided at index `i`
(where `0 <= i <= n)` into two arrays (possibly empty) `numsₗₑfₜ` and `numsᵣᵢgₕₜ`:

- `numsₗₑfₜ` has all the elements of `nums` between index `0` and `i - 1` **(inclusive)**, while
`numsᵣᵢgₕₜ` has all the elements of nums between index `i` and `n - 1` **(inclusive)**.
- If `i == 0`, `numsₗₑfₜ` is **empty**, while `numsᵣᵢgₕₜ` has all the elements of `nums`.
- If `i == n`, `numsₗₑfₜ` has all the elements of nums, while `numsᵣᵢgₕₜ` is **empty**.

The **division score** of an index `i` is the **sum** of the number of `0`'s in `numsₗₑfₜ` and the
number of `1`'s in `numsᵣᵢgₕₜ`.

Return **all distinct indices** that have the **highest** possible **division score**. You may
return the answer in **any order**.

**Example 1:**

```
Input: nums = [0,0,1,0]
Output: [2,4]
Explanation: Division at index
- 0: numsₗₑfₜ is []. numsᵣᵢgₕₜ is [0,0,1,0]. The score is 0 + 1 = 1.
- 1: numsₗₑfₜ is [0]. numsᵣᵢgₕₜ is [0,1,0]. The score is 1 + 1 = 2.
- 2: numsₗₑfₜ is [0,0]. numsᵣᵢgₕₜ is [1,0]. The score is 2 + 1 = 3.
- 3: numsₗₑfₜ is [0,0,1]. numsᵣᵢgₕₜ is [0]. The score is 2 + 0 = 2.
- 4: numsₗₑfₜ is [0,0,1,0]. numsᵣᵢgₕₜ is []. The score is 3 + 0 = 3.
Indices 2 and 4 both have the highest possible division score 3.
Note the answer [4,2] would also be accepted.
```

**Example 2:**

```
Input: nums = [0,0,0]
Output: [3]
Explanation: Division at index
- 0: numsₗₑfₜ is []. numsᵣᵢgₕₜ is [0,0,0]. The score is 0 + 0 = 0.
- 1: numsₗₑfₜ is [0]. numsᵣᵢgₕₜ is [0,0]. The score is 1 + 0 = 1.
- 2: numsₗₑfₜ is [0,0]. numsᵣᵢgₕₜ is [0]. The score is 2 + 0 = 2.
- 3: numsₗₑfₜ is [0,0,0]. numsᵣᵢgₕₜ is []. The score is 3 + 0 = 3.
Only index 3 has the highest possible division score 3.
```

**Example 3:**

```
Input: nums = [1,1]
Output: [0]
Explanation: Division at index
- 0: numsₗₑfₜ is []. numsᵣᵢgₕₜ is [1,1]. The score is 0 + 2 = 2.
- 1: numsₗₑfₜ is [1]. numsᵣᵢgₕₜ is [1]. The score is 0 + 1 = 1.
- 2: numsₗₑfₜ is [1,1]. numsᵣᵢgₕₜ is []. The score is 0 + 0 = 0.
Only index 0 has the highest possible division score 2.
```

**Constraints:**

- `n == nums.length`
- `1 <= n <= 10⁵`
- `nums[i]` is either `0` or `1`.
