class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue_r = deque()
        queue_d = deque()


        for i , char in enumerate(senate):
            if char == 'D':
                queue_d.append(i)

            else:
                queue_r.append(i)

        while queue_r and queue_d:
            if queue_r[0] > queue_d[0]:
                queue_r.popleft()
                index = queue_d.popleft()
                queue_d.append(index + len(senate))

            else:
                queue_d .popleft()
                index = queue_r.popleft()
                queue_r.append(index + len(senate))

        if queue_r:
            return 'Radiant'

        return 'Dire'


        















        # stack = []

        # for i , char in enumerate(senate):
        #     if stack and char != stack[-1][0]:
        #         if stack[-1][1] == 1:
        #             stack[-1][1] = 0

        #         else:
        #             stack.pop()
        #             if stack and stack[-1][1] == 1:
        #                 stack[-1][1] = 0
        #             else:
        #                 stack.append([char, 0])

        #     else:
        #         stack.append([char, 1])
        # if stack[-1][0] == "R":
        #     return 'Radiant'

        # return 'Dire'



        