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
- https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/ *
- https://leetcode.com/problems/3sum/ *


## Binary Search 
Binary Search is defined as a searching algorithm used in a sorted array by repeatedly dividing the search interval in half. The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(log N). 
```python
def binary_search(array, target):
    # if target in nums:
    #     return nums.index(target)
    # return -1
    ############ Bruteforce
    # count = 0

    # while count < len(nums):
    #     if nums[count] == target:
    #         return count
    #     count += 1

    # return -1
    ############ Binary
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

Leetcode problems:
- https://leetcode.com/problems/binary-search/
- https://leetcode.com/problems/search-a-2d-matrix/ *
- https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
- https://leetcode.com/problems/search-in-rotated-sorted-array/
- https://leetcode.com/problems/time-based-key-value-store/


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
