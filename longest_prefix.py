class Solution:
    def __init__(self, strs):
        self.strs = strs
        
    def call(self):
        if len(self.strs) == 0:
            return ""
        
        strs = sorted(self.strs, key=len) 
        first = strs[0]   
        first_length = len(first)
        
        prefixes = [ first[:i] for i in range(1, first_length+1)]
        
        answer = [ first[:i] for i in range(1, first_length+1)]
        
        for s in strs[1:]:
            for i in range(first_length):
                if s[:i+1] != prefixes[i] and prefixes[i] in answer:
                    answer.remove(prefixes[i])
                    
        print(answer)
                    
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

