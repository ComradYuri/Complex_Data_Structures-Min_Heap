# Min_Heap
MinHeap tracks the minimum element as the element at index 1 within an internal Python list.

When adding elements, we use .heapify_up() to compare the new element with its parent, 
making swaps if it violates the heap property: children must be greater than their parents.

When removing the minimum element, we swap it with the last element in the list. 
Then we use .heapify_down() to compare the new root with its children, swapping with the smaller child if necessary.

Heaps are so useful because they're efficient in maintaining their heap properties.

Example of efficiency:
Output:
ADDING!
Heap of 10001 elements restored with 13 swaps

REMOVING!
Heap of 10000 elements restored with 13 swaps
