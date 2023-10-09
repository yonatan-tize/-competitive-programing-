class Solution:
    def frequencySort(self, s: str) -> str:
        my_dict = dict()
        ans = list()
        result = '' 
        for char in s:
            my_dict[char] = my_dict.get(char, 0) + 1
        for key, value in my_dict.items():
            ans.append((value, key))

        ans.sort(reverse=True)

        for i, k in ans:
            result += k * i
            i += 1
        return result



        