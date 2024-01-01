class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        g = set()
        w = set()
        seen = set()
        for r, c in walls:
            w.add((r,c))

        for r, c in guards:
            g.add((r,c))

        for i,j in g:
            r = i-1
            c = j
            while r > -1 and ((r,c) not in g) and ((r,c) not in w): # going north
                seen.add((r,c))
                r -= 1

            r = i+1
            c = j
            while r < m and ((r,c) not in g) and ((r,c) not in w): # going south
                seen.add((r,c))
                r += 1

            r = i
            c = j - 1
            while c > -1 and ((r,c) not in g) and ((r,c) not in w): # going west
                seen.add((r,c))
                c -= 1

            r = i
            c = j + 1
            while c < n and ((r,c) not in g) and ((r,c) not in w):# going east
                seen.add((r,c))
                c += 1
        return m*n - len(seen) - len(g) - len(w) 


        