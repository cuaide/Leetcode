class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k # KthLargest
        self.heap = nums
    def add(self, val: int) -> int:
        self.heap.append(val) #3->5->10->9->4
        self.heap.sort() #2,3,4,5,8
        return self.heap[len(self.heap)-self.k]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)