class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        count = 1
        start, end = points[0][0], points[0][1]

        for i in range(1, len(points)):
            curr_start, curr_end = points[i]

            start = max(start, curr_start)
            end = min(end, curr_end)

            if start > end:
                count += 1
                start = curr_start
                end = curr_end
                continue


        return count