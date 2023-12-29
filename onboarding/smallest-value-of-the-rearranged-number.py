class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        sign = -1 if num < 0 else 1
        s = str(abs(num))
        countZero = 0
        store = []
        for n in s:
            if n == '0':
                countZero += 1
            else:
                store.append(n)
            
        if sign == -1:
            store.sort(reverse = True)
            number = ''.join(store) + '0' * countZero
            return -1 * int(number)
        else:
            store.sort()
            number = store[0] + '0' * countZero + ''.join(store[1:])
            return int(number)
