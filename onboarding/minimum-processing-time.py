class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()
        j = 0
        ans = 0
        for i in range(len(tasks)-1, 0, -4):
            k = i
            count = 0
            processor = processorTime[j]
            while k > i - 4:
                count = max(processor + tasks[k], count)
                k -= 1
            j += 1
            ans = max(ans, count)
        return ans





        