class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            max_num = max(firstList[i][0], secondList[j][0])
            min_num = min(firstList[i][1], secondList[j][1])

            if max_num <= min_num:
                ans.append([max_num, min_num])

            if min_num == firstList[i][1] and min_num == secondList[j][1]:
                i += 1
                j += 1

            elif min_num == firstList[i][1]:
                i += 1
            else:
                j += 1

        return ans
            

                







