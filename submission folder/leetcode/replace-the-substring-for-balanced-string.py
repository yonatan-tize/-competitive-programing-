class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        frequancy = len(s)//4
        ans = len(s)+1
        excess = defaultdict(int)
        for key, value in count.items():
            if value > frequancy:
                excess[key] = value - frequancy

        if not excess:
            return 0
        left = 0
        for right, char in enumerate(s):
            if char in excess:
                excess[char] -= 1

                while max(excess.values()) <= 0:
                    ans = min(ans, right-left+1)
                    if s[left] in excess:
                        excess[s[left]] += 1
                    left += 1
                
        return ans 

            


                
