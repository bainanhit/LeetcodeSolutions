# T1 小美抓敌人

# 二维前缀和
n, a, b = map(int, input().split())
mp = [[0]*1001 for i in range(1001)]
for i in range(n):
    x, y = map(int, input().split())
    mp[x][y] += 1  #在地图内计数
for i in range(1, 1001):
    for j in range(1, 1001):
        mp[i][j] += mp[i-1][j] + mp[i][j-1] - mp[i-1][j-1]  #前缀和初始化
        ans = 0
for i in range(a+1, 1001): #枚举右上端点
    for j in range(b+1, 1001):  #此时枚举的矩形为 (i-a, j-b) 到 (i,j)之间的矩形
        t = mp[i][j] - mp[i-a-1][j] - mp[i][j-b-1] + mp[i-a-1][j-b-1]
ans = max(ans, t)
print(ans)


# t2 k彩色区间

# 滑动窗口
# 当右端点遇到一个新的数,dif+1,当左端点删去一个只出现一次的数时,dif-1
from collections import defaultdict
n , k = list(map(int , input().split()))
a = list(map(int , input().split()))
res = 0
i = 0
j = 0
# 记录每个数出现次数
num_count = defaultdict(int)
# 记录当前区间的不同数的个数
dif = 0
# 双指针
while j < n:
    num_count[a[j]] += 1
    # 遇到新的数
    if num_count[a[j]] == 1:
        dif += 1
    while dif > k:
        # 删去只出现一次的数
        if num_count[a[i]] == 1:
            dif -= 1
        num_count[a[i]] -= 1
        i += 1
    res = max(res , j - i + 1)
    j += 1
print (ans)


