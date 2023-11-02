def binarySearch(arr, target):
    start, end = 0, len(arr)-1

    while start <= end:
        mid = (start+end)//2
        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
            
    return start

def smallerNumbers(nums1, nums2):
    ans = []
    for num in nums2:
        count = binarySearch(nums1, num)
        ans.append(count)
    return ans

n, m = map(int, input().split())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))


ans = smallerNumbers(nums1, nums2)
ans = list(map(str, ans))
ans = " ".join(ans)

print(ans)
