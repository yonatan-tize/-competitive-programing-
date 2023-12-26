class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            swapped = False
            for j in range(1,len(names)-i):
                if heights[j] > heights[j-1]:
                    names[j], names[j-1] = names[j-1], names[j]
                    heights[j], heights[j-1] = heights[j-1], heights[j] 
                    swapped = True
            if not swapped:
                return names
        return names