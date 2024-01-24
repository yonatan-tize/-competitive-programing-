class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        psum = [0] * 1000
        for nump, start, end in trips:
            if end < 1000:
                psum[end] -= nump
            psum[start] += nump

        if psum[0] > capacity:
            return False
        for i in range(1,len(psum)):
            psum[i] += psum[i-1]
            if psum[i] > capacity:
                return False
        return True

        
            

            