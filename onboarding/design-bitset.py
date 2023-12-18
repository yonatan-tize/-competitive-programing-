class Bitset:

    def __init__(self, size: int):
        self.size = size
        self.bitset = ['0'] * self.size
        self.count1 = 0
        self.flipcount = 0
        
    def fix(self, idx: int) -> None: #Updates the bit at the index to 1 if 0
        if self.flipcount % 2 != 0:
            if self.bitset[idx] == '1':
                self.count1 += 1
                self.bitset[idx] = '0'
        else:
            if self.bitset[idx] == '0':
                self.count1 += 1
                self.bitset[idx] = '1' 

    def unfix(self, idx: int) -> None:#Updates the bit at the index to 0 if 1
        if self.flipcount % 2 != 0:
            if self.bitset[idx] == '0':
                self.count1 -= 1
                self.bitset[idx] = '1'
        else:
            if self.bitset[idx] == '1':
                self.count1 -= 1
                self.bitset[idx] = '0' 


    def flip(self) -> None: #fliping the value 
        self.flipcount += 1
        self.count1 = self.size - self.count1

    def all(self) -> bool:# if all the numbers are 1
        if self.size == self.count1:
            return True
        return False

    def one(self) -> bool: # at least one 1
        if self.count1 > 0:
            return True
        return False

    def count(self) -> int: # number of one
        return self.count1

    def toString(self) -> str: 
        if self.flipcount % 2 == 0:
            return ''.join(self.bitset)
        else:
            s = ''
            for i in range(self.size):
                if self.bitset[i] == '1':
                    s += '0'
                else:
                    s += '1'
        return s

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()