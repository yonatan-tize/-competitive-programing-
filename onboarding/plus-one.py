class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carrier = 1
        last = digits[0]
        print(last)
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 9:
                digits[i] = 0
                print(digits)
            else:
                digits[i] += carrier
                return digits
        print(digits[0])
        print(last)
        
        if digits[0] != last:
            a = [1]
            a.extend(digits)
            
            return a
        return digits