# O(Nlogn) Z(n)
def merge(arr, left_lst, right_lst):
    l, r = 0, 0
    new_lst = []
    while l < len(left_lst) and r < len(right_lst):
        if left_lst[l] <= right_lst[r]:
            new_lst.append(left_lst[l])
            l += 1
        else:
            new_lst.append(right_lst[r])
            r += 1
    new_lst += left_lst[l:]
    new_lst += right_lst[r:]

    return new_lst

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_lst = merge_sort(arr[: mid])
    right_lst = merge_sort(arr[mid:])

    return merge(left_lst, right_lst)

