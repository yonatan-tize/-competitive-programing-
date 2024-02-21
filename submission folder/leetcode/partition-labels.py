class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index_map = {}
        ans = []

        for i in range(len(s)):
            index_map[s[i]] = i

        curr_max = 0 
        l = 0
        for i in range(len(s)):
            curr_max = max(curr_max, index_map[s[i]])
            if curr_max == i:
                ans.append(i-l + 1)
                l = i + 1

        return ans

            

        print(index_map)