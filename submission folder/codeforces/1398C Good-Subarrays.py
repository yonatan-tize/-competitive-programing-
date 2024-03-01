t = int(input())
for _ in range(t):
    length = int(input())
    n = input()
    nums = list(map(int, list(n)))
    nums = [num-1 for num in nums]
    store = {0:1}
    curr = 0
    ans = 0

    for i in range(length):
        curr += nums[i]
        if curr in store:
            ans += store[curr]

        store[curr] = store.get(curr, 0) + 1

    print(ans)