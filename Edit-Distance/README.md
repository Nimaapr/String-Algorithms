# Edit Distance Algorithms

## Overview
The Edit Distance (or Levenshtein distance) algorithms in this directory provide solutions to measure the difference between two strings. This is done by calculating the minimum number of operations (insertions, deletions, substitutions) required to transform one string into another. This directory contains two versions of the Edit Distance algorithm:
1. A standard dynamic programming approach.
2. A memory-efficient dynamic programming approach.

## Algorithms

### 1. Standard Dynamic Programming Approach
- **File**: `edit_distance.py`
- This version uses a 2D matrix to store the results of subproblems, making it easy to understand and trace the algorithm's steps.
- **Complexity**:
  - Time Complexity: O(mn), where m and n are the lengths of the two strings.
  - Space Complexity: O(mn), due to the 2D array used for storing intermediate results.

### 2. Memory-Efficient Dynamic Programming Approach
- **File**: `edit_distance_memory_efficient.py`
- This version optimizes space usage by using two 1D arrays and swapping them after each iteration, significantly reducing the space requirement.
- **Complexity**:
  - Time Complexity: O(mn), similar to the standard approach.
  - Space Complexity: O(min(m, n)), as it uses two arrays of size equal to the smaller of the two string lengths.

## Requirements
- Python 3.x

## Usage
To use these scripts, run them with Python and provide two strings for which you want to calculate the edit distance. For example:
```python
# For the standard approach
from edit_distance import editDistance as editDistanceStandard
print(editDistanceStandard("kitten", "sitting"))

# For the memory-efficient approach
from edit_distance_memory_efficient import editDistance as editDistanceMemoryEfficient
print(editDistanceMemoryEfficient("kitten", "sitting"))
