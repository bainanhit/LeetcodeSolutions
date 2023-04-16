import random

'''
解法：我们总是选择第一个对象，以1/2的概率选择第二个，以1/3的概率选择第三个，
以此类推，以1/m的概率选择第m个对象。当该过程结束时，每一个对象具有相同的选中概率
'''

# 对于第i个元素（i>k），出现在池中的概率与池中元素留下的概率相同，为k/i=k/n
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
samples = []
k = 5
cur_len = k

# 第i个元素 <= k时，直接进入池中
for i in range(k):
    samples.append(num[i])
# 第i个元素 > k时,以k / i的概率进入池中
for i in range(k, len(nums)-1):
    # cur_len += 1
    rand = random.randint(1, i+1)
    if rand < k:
        # 替换
        samples[rand-1] = nums[i]

        
    
