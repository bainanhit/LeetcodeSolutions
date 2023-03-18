class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        # 差分数组，离散化
        diff = defaultdict(int)
        # 差分状态存储
        for start, end in flowers:
            diff[start] += 1
            diff[end+1] -= 1
        times = sorted(diff.keys())

        n = len(persons)
        res = [0] * n
        i, sum_ = 0, 0
        ids = [num for num in range(n)]
  
        zip_ = sorted(list(zip(persons, ids)), key=lambda x:x[0], reverse=False)
        for p, idx in zip_:
            while i < len(times) and times[i] <= p:
                sum_ += diff[times[i]]
                i += 1
            res[idx] = sum_
        return res
        
        