class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        occur = {}
        res = []
        for i in range(len(list1)):
            if list1[i] in list2:
                occur[list1[i]] = i + list2.index(list1[i])
        min_occur = min(occur.values())
        for i in occur:
            if occur[i] == min_occur:
                res.append(i)
        return res
        
            
            

