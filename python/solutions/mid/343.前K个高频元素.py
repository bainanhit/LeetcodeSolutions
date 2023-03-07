import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 小顶堆实现
        map_ = {}
        for num in nums:
            map_[num] = map_.get(num, 0) + 1   

        pri_que = []
        for key, val in map_.items():
            heapq.heappush(pri_que, (val, key))
            if len(pri_que) > k:
                heapq.heappop(pri_que)

        res = [0] * k
    
        for i in range(k-1, -1, -1):
            res[i] = heapq.heappop(pri_que)[1]
        
        return res
                
