class ATM:

    def __init__(self):
        self.index = [20, 50, 100, 200, 500]
        self.money = [0] * len(self.index)

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(self.index)):
            self.money[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        ans = [0] * len(self.index)
        for i in reversed(range(len(ans))):
            ans[i] = min(amount // self.index[i], self.money[i])
            amount -= ans[i] * self.index[i]
            
        if amount:
            return [-1]
        else:
            for i in range(len(ans)):
                self.money[i] -= ans[i]
            return ans


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)