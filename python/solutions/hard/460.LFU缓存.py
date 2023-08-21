class LFUCache:
    # 双hash表
    # O(1) Z(cap)
    # key与freq映射，为了找key在哪个频率下；
    # key与value映射，为了找key对应的value值，这个需要一个有序字典OrderedDict，为了好弹出同一个频率下，最开始加入的key（当然是容量不够，需要弹出的时候）

    def __init__(self, capacity: int):
        from collections import OrderedDict, defaultdict
        self.freq = defaultdict(OrderedDict)
        self.key_to_freq = {}
        self.capacity = capacity
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_to_freq:
            return -1
        key_freq = self.key_to_freq[key]
        res = self.freq[key_freq].pop(key)
        if not self.freq[key_freq] and key_freq == self.min_freq:
            self.min_freq += 1
        self.freq[key_freq + 1][key] = res
        self.key_to_freq[key] = key_freq + 1
        return res

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        # key 本身就在其中
        if key in self.key_to_freq:
            key_freq = self.key_to_freq[key]
            self.freq[key_freq].pop(key)
            if not self.freq[key_freq] and key_freq == self.min_freq:
                self.min_freq += 1
            self.freq[key_freq + 1][key] = value
            self.key_to_freq[key] = key_freq + 1
        else:
            # key不在, 要弹出频率使用次数少的key
            if len(self.key_to_freq) == self.capacity:
                k, v = self.freq[self.min_freq].popitem(last=False)
                self.key_to_freq.pop(k)
            self.key_to_freq[key] = 1
            self.freq[1][key] = value
            self.min_freq = 1


# 链接：https://leetcode.cn/problems/lfu-cache/solutions/188710/\yi-zhang-tu-shuo-ming-bai-by-powcai/
