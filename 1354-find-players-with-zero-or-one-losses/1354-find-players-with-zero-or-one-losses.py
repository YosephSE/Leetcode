class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        map = {}
        res = [[], []]
        for item in matches:
            if item[0] not in map:
                map[item[0]] = 0
            if item[1] in map:
                map[item[1]] -= 1
            else:
                map[item[1]] = -1
        for item in map:
            if map[item] == 0:
                res[0].append(item)
            elif map[item] == -1:
                res[1].append(item)
        res[0] = sorted(res[0])
        res[1] = sorted(res[1])
        return res
        

        
        