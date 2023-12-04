class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        step = 0
        curr_capacity = capacity 
        for i, num in enumerate(plants):
            if  curr_capacity - num < 0:
                step += (2*i + 1)
                curr_capacity = capacity - num
            else:
                step += 1
                curr_capacity -= num
        return step


