# Distinct Subsequences

## Overview
The "Distinct Subsequences" project provides Python solutions for counting the number of distinct subsequences of a string that equal another string. This problem is a classic example of dynamic programming. The repository includes both a standard implementation and a memory-efficient version.

## Problem Statement
Given two strings `s` and `t`, the task is to count the number of distinct subsequences of `s` which equals `t`. A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters.

## Implementations

### 1. Standard Dynamic Programming Approach
- **File**: `Distinct_subsequences.py`
- This version uses a 2D matrix for dynamic programming, storing results for all sub-problems.
- **Complexity**:
  - **Time Complexity**: O(mn), where m is the length of string `s` and n is the length of string `t`.
  - **Space Complexity**: O(mn), due to the 2D array for storing the dynamic programming states.

### 2. Memory-Efficient Dynamic Programming Approach
- **File**: `Distinct_subsequences_efficient.py`
- This version optimizes space by using only two 1D arrays that are updated for each character of `s`.
- **Complexity**:
  - **Time Complexity**: O(mn), similar to the standard approach.
  - **Space Complexity**: O(n), significantly reduced from the standard approach by using only two 1D arrays.

## Usage
To run these scripts, use Python to execute the desired file and provide the input strings `s` and `t`. For example:
```python
# For the standard approach
from Distinct_subsequences import numDistinct
print(numDistinct("rabbbit", "rabbit"))

# For the memory-efficient approach
from Distinct_subsequences_efficient import numDistinct
print(numDistinct("rabbbit", "rabbit"))
