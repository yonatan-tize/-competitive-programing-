m = input()
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))
ans = []
i1, i2 = 0, 0

while i1 < len(nums1) and i2 < len(nums2):
    if nums1[i1] <= nums2[i2]:
        ans.append(nums1[i1])
        i1 += 1
    else:
        ans.append(nums2[i2])
        i2 += 1

while i1 < len(nums1):
    ans.append(nums1[i1])
    i1 += 1

while i2 < len(nums2):
    ans.append(nums2[i2])
    i2 += 1

ans = list(map(str, ans))
ans = " ".join(ans)
print(ans)






