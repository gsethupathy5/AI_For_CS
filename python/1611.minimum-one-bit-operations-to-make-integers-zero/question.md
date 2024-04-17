# [1611. Minimum One Bit Operations to Make Integers Zero][link] (Hard)

[link]: https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/

Given an integer `n`, you must transform it into `0` using the following operations any number of
times:

- Change the rightmost ( `0ᵗʰ`) bit in the binary representation of `n`.
- Change the `iᵗʰ` bit in the binary representation of `n` if the `(i-1)ᵗʰ` bit is set to `1` and the
`(i-2)ᵗʰ` through `0ᵗʰ` bits are set to `0`.

Return the minimum number of operations to transform  `n` into  `0`.

**Example 1:**

```
Input: n = 3
Output: 2
Explanation: The binary representation of 3 is "11".
"11" -> "01" with the 2ⁿᵈ operation since the 0ᵗʰ bit is 1.
"01" -> "00" with the 1ˢᵗ operation.
```

**Example 2:**

```
Input: n = 6
Output: 4
Explanation: The binary representation of 6 is "110".
"110" -> "010" with the 2ⁿᵈ operation since the 1ˢᵗ bit is 1 and 0ᵗʰ through 0ᵗʰ bits are 0.
"010" -> "011" with the 1ˢᵗ operation.
"011" -> "001" with the 2ⁿᵈ operation since the 0ᵗʰ bit is 1.
"001" -> "000" with the 1ˢᵗ operation.
```

**Constraints:**

- `0 <= n <= 10⁹`
