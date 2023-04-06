class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # 递增单调栈, 用双端队列实现
        deque = collections.deque()
        n = len(num)
        for c in num:
            # 当且仅当K>0 并且队尾元素大于要入队的元素的时候就把队尾元素移除掉
            while k and deque and deque[-1] > c:
                deque.pop()
                k -= 1
            deque.append(c)
        # 此时如果K还大于0 队列里面的元素已经为单调不降了。则最后依次移除队列尾部剩余的k数次即可
        for i in range(k):
            deque.pop()
        # 从队列取出元素
        res = ''
        flag = 1
        while deque:
            ch = deque.popleft()
            # 消除前导0
            if flag and ch == '0':
                continue
            flag = 0
            res += ch
        
        return '0' if len(res)==0 else res

