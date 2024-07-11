Search:
**Binary search** - Runtime O(log N) avg and worst runtimes, best O(1)

  Explanation: Each time you are comparing the middle of the array to the target and discarding half of the array. 
  If you keep dividing and only searching in half until you either find the target or it is not there - that is log<sub>2</sub>(N).      Therefore, log(N) shows the runtime as the input size grows = time complexity.
               
  The best runtime is if your target is the first element you choose/middle of the array.
  
  _Notes:_
    1. search on a sorted array/sorted balanced tree is the same
    2. completely skewed tree (all elements are on the right or left) would be O(N)

Sorts:
1. **Selection Sort** - Runtime O(N<sup>2</sup>) in all cases, since we are traversing the array for each spot in the array to check for a minimum element
  Explanation: Has 2 pointers, 1 starts at the beginning of the array and the second looks in the remaining spots in the array for the   minimum element. If found, it swaps that element with the element at the first pointer. The first pointer then increments to the       second spot and the search repeats for the minimum element. This pattern continues until the first pointer reaches the end of the      array, which will have the largest element left.

2. **Merge Sort** - Runtime O(N log(N)) in all cases, since we divide the array recursively in half = log(N) and linearly (N) merge the
   halves back in sorted order.

   Explanation: Keep an empty array for the sorted elements. Divide the unsorted array into halves until each element is alone in its     array. Now that it is sorted (when it is the only element then it is by default sorted), we can merge the sorted arrays together in    sorted order by comparing the elements in each subarray (there will be 2) at the first index of the element not yet in the sorted      array; the smaller element will be placed in the array and both the subarray index and the sorted array index will be incremented.
