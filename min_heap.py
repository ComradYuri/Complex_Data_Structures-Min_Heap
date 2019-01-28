class MinHeap:
    def __init__(self):
        # zeroth index is set at None for easier building of min heap
        self.heap_list = [None]
        # zeroth index (None) is not counted. Now counting starts
        self.count = 0

    # HEAP HELPER METHODS
    # parent index is always the floor division 2 of child index
    def parent_idx(self, idx):
        return idx // 2
    # left child index is always double the parent index

    def left_child_idx(self, idx):
        return idx * 2

    # right child index is always double + 1 of the parent index
    def right_child_idx(self, idx):
        return idx * 2 + 1

    # checks if a a parent has children. If not it's not a parent but a leaf
    def child_present(self, idx):
        return self.left_child_idx(idx) <= self.count

    # returns top item of min heap (the minimal value) and heaps down to restore the rules of a min heap
    def retrieve_min(self):
        if self.count == 0:
            print("No items in heap")
            return None

        min = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.count]
        self.count -= 1
        self.heap_list.pop()
        self.heapify_down()
        return min

    # adds new element in the correct place with heapifying up
    def add(self, element):
        self.count += 1
        self.heap_list.append(element)
        self.heapify_up()

    # Firstly looks if there is a right child. If not it returns the left child index.
    # If both are present it returns the index of the smallest child
    def get_smaller_child_idx(self, idx):
        if self.right_child_idx(idx) > self.count:
            return self.left_child_idx(idx)
        else:
            left_child = self.heap_list[self.left_child_idx(idx)]
            right_child = self.heap_list[self.right_child_idx(idx)]
            if left_child < right_child:
                return self.left_child_idx(idx)
            else:
                return self.right_child_idx(idx)

    # Starts at last element of the heap list and swaps until min heap values are met
    def heapify_up(self):
        idx = self.count
        swap_count = 0
        while self.parent_idx(idx) > 0:
            if self.heap_list[self.parent_idx(idx)] > self.heap_list[idx]:
                swap_count += 1
                tmp = self.heap_list[self.parent_idx(idx)]
                self.heap_list[self.parent_idx(idx)] = self.heap_list[idx]
                self.heap_list[idx] = tmp
            idx = self.parent_idx(idx)

        element_count = len(self.heap_list)
        if element_count > 10000:
            print("Heap of {0} elements restored with {1} swaps"
                  .format(element_count, swap_count))
            print("")

    # Starts at first element of the heap list and swaps until min heap values are met
    def heapify_down(self):
        idx = 1
        # starts at 1 because we swapped first and last elements
        swap_count = 1
        while self.child_present(idx):
            smaller_child_idx = self.get_smaller_child_idx(idx)
            if self.heap_list[idx] > self.heap_list[smaller_child_idx]:
                swap_count += 1
                tmp = self.heap_list[smaller_child_idx]
                self.heap_list[smaller_child_idx] = self.heap_list[idx]
                self.heap_list[idx] = tmp
            idx = smaller_child_idx

        element_count = len(self.heap_list)
        if element_count >= 10000:
            print("Heap of {0} elements restored with {1} swaps"
                  .format(element_count, swap_count))
            print("")
