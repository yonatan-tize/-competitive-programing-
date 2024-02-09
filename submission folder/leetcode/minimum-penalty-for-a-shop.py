class Solution:
    def bestClosingTime(self, customers: str) -> int:
        psum = [0] * len(customers)
        n = len(customers)
        y = customers.count('Y')
        x = 0

        for i in range(n):
            psum[i] += y
            if customers[i] == 'Y':
                y -= 1
            psum[i] += x
            if customers[i] == 'N':
                x += 1

        index = 0
        min_cust = psum[0]
        psum.append(x)
        for k in range(n+1):
            if psum[k] < min_cust:
                min_cust = psum[k]
                index = k
    
        return index







# pre = []
#         post = []
#         n = len(customers)
#         y = customers.count('Y')
#         x = 0

#         for i in range(n):
#             post.append(y)
#             if customers[i] == 'Y':
#                 y -= 1
#             pre.append(x)
#             if customers[i] == 'N':
#                 x += 1

#         index = 0
#         min_cust = post[0] + pre[0]
#         post.append(x)
#         for k in range(n+1):
#             if k < n:
#                 post[k] += pre[k]
#             if post[k] < min_cust:
#                 min_cust = post[k]
#                 index = k
    
#         return index


        