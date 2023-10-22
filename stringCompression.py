class Solution:
    def compress(self, chars: List[str]) -> int: 
        i = j = 0

        while j < len(chars):
            
            if chars[j] != chars[i]:
                l = j - i 
                if l > 1:
                    for n in str(l):
                        i += 1
                        chars[i] = n
                i += 1
                chars[i] = chars[j]

            j += 1

        l = j - i 
        if l > 1:
            for n in str(l):
                i += 1
                chars[i] = n
        
        return i + 1
    
