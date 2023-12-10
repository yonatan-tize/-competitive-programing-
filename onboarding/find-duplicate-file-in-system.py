class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for directory in paths:
            path = directory.split()
            for i in range(1,len(path)):
                file = path[i]
                name, content = file.split('(')
                dict[content].append(path[0]+'/' + name)
                
        return [value for value in dict.values() if len(value) > 1]
        

            