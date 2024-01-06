class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1
            else:
                return False

        while j < len(typed):
            if j > 0 and typed[j] == typed[j-1]:
                j += 1
            else:
                return False
        return len(typed) == j and len(name) == i