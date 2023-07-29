## Two Pointers 

Check if string is Palindrome, using two pointers.
Two pointers are used to check both ends of the string/array
```python
def two_pointers(array):

    start = 0
    end = len(array) - 1

    while start <= end:

        if array[start] != array[end]:
            return False

        start += 1
        end -= 1
    return True
```

Leetcode problems:
- https://leetcode.com/problems/reverse-string/
- https://leetcode.com/problems/valid-palindrome/
- https://leetcode.com/problems/merge-sorted-array/ *


## Binary Search 

## Sliding Window

## Fast+Slow Pointers 

Leetcode problems:
- https://leetcode.com/problems/linked-list-cycle/

## Merging Intervals 

## Sorting 

## Linked List Reversal 

## BFS 

## Recursion 

## DFS 

## Topological Sort 

## Memoization 

## DP
