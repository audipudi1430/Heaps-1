# Approach:
# - Maintain a Min-Heap of size k: Push each number into the heap and pop the smallest if the heap size exceeds k.
# - The top of the heap (smallest element) will be the kth largest element after processing all numbers.
# - More efficient than sorting when k is much smaller than n, as it avoids full array sorting.
#
# Time Complexity: O(n log k), where n is the number of elements in nums.
# Space Complexity: O(k), for storing at most k elements in the heap.

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0]
