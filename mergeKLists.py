# Approach:
# - Use a Min-Heap to always extract the smallest node among all the current heads of the k lists.
# - Push the next node from the extracted node's list into the heap to continue merging.
# - Build the final merged linked list by connecting nodes in sorted order.
#
# Time Complexity: O(N log k), where N is the total number of nodes and k is the number of lists.
# Space Complexity: O(k), for storing up to k nodes in the heap.

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        
        # Initialize heap
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, idx, node))
        
        dummy = ListNode(0)
        curr = dummy
        
        while minHeap:
            val, idx, node = heapq.heappop(minHeap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(minHeap, (node.next.val, idx, node.next))
        
        return dummy.next
