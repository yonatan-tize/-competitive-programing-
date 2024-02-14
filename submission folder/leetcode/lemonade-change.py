class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        num_five = 0
        num_ten = 0
        for i in range(len(bills)):
            if bills[i] == 5:
                num_five += 1

            elif bills[i] == 10:
                if num_five > 0:
                    num_five -= 1
                    num_ten += 1
                else:
                    return False

            else:
                if num_ten > 0:
                    num_ten -= 1
                    bills[i] -= 10
                if bills[i] == 10:
                    if num_five > 0:
                        num_five -= 1
                    else:
                        return False

                else:
                    if num_five > 2:
                        num_five -= 3

                    else:
                        return False

        return True

                

