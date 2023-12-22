class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            i, j = 0, len(row)-1
            while i <= j:
                if i == j:
                    row[j] = 1 if row[j] == 0 else 0
                    break
                    
                row[i], row[j] = row[j], row[i]
                row[i] = 1 if row[i] == 0 else 0
                row[j] = 1 if row[j] == 0 else 0
                i += 1
                j -= 1
        return image
        