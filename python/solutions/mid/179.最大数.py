class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def comp(x, y):
            a, b = int(x+y), int(y+x)
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0
        
        lst = list(map(str, nums))

        lst.sort(key=cmp_to_key(comp), reverse=True)

        return ''.join(lst) if lst[0] != '0' else '0'
