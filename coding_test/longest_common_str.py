class Solution:
    def __init__(self, strs):
        self.strs = strs
        
    def call(self):
        if len(self.strs) == 0:
            return ""
        
        strs = sorted(self.strs, key=len) 
        first = strs[0]   
        first_length = len(first)
        
        from itertools import combinations
        
        first_combinations = []
        combination_num = 1
        
        while (combination_num <= first_length):
            tmp = combinations(first, combination_num)
            first_combinations += tmp
            combination_num += 1
        
        default = [ "".join(e) for e in first_combinations]
        answer = [ "".join(e) for e in first_combinations]
        
        for s in strs[1:]:
            for c in default:
                if c not in s and c in answer:
                        answer.remove(c)

        if len(answer) == 0:
            return ""
        
        else:
            return sorted(answer, key=len, reverse=True)[0]
        

case1 = ["flower","flow","flight"]

case2 = ["cir","car"]

case3 = ["dog","racecar","car"]

case4 = ["reflower","flow","flight"]

print(Solution(case1).call())

print(Solution(case2).call())

print(Solution(case3).call())

print(Solution(case4).call())

