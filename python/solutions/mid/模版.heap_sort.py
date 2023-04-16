
def max_heap(nums, start, n):

    # lef root t孩子节点索引
    left = start*2 + 1 
    while left <= n:
    # 节点有右子节点，并且右子节点的值大于左子节点，则将child变为右子节点的索引
        if left+1 < n and nums[l] < nums[left+1]:
            left += 1
        if nums[start] < nums[left]:
            nums[start], nums[left] = nums[left], nums[start]
            # 交换值后，如果存在孙节点，则将root设置为子节点，继续与孙节点进行比较
            start = left
            left = start*2 + 1
        else:
            break

def heap_sort(nums):
    first = len(nums)//2 - 1
    n = len(nums)
    # 从下到上，从右到左对每个非叶节点进行调整，循环构建成大顶堆
    for start in range(first, -1, -1):
        max_heap(nums, start, n-1)
    # 交换堆顶和堆尾的数据
    for end in range(n-1, 0, -1):
        nums[0], nums[end] = nums[end], nums[0]
        # 重新调整完全二叉树，构造成大顶堆
        max_heap(nums, 0, n-1)
        
    return nums
