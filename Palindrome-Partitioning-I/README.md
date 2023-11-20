# Palindrome Partitioning I Solutions

## Project Overview
This repository contains two Python solutions for the Palindrome Partitioning I problem. The goal is to partition a given string such that every substring in the partition is a palindrome. The repository includes a basic backtracking solution and an optimized solution using dynamic programming.

## Solutions
1. `palindrome_partitioning_recursive.py`: Implements a straightforward backtracking approach to generate all possible palindrome partitions.
2. `palindrome_partitioning_dp.py`: Utilizes dynamic programming to optimize palindrome checking, reducing redundant computations.

## Complexity Analysis

### Backtracking Solution
- **File**: `palindrome_partitioning_recursive.py`
- **Time Complexity**: O(2^n), where n is the length of the string.
- **Space Complexity**: O(2^n), due to storage for partitions and recursion stack.

### Dynamic Programming Solution
- **File**: `palindrome_partitioning_DP.py`
- **Time Complexity**: Improved compared to backtracking. O(n^2) for pre-computation and reduced time for backtracking.
- **Space Complexity**: O(n^2), mainly for the DP table and O(n) for the recursion stack.

## Requirements
- Python 3.x