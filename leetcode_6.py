class Solution:  ## not completed
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s
        
        N = 2*numRows-2
        # 3 -> 4
        # 4 -> 6
        # 5 -> 8
        
        LENGTH = len(s) 
        column = (numRows-1)*((LENGTH + N - 1) // N)
            
        zero_matrix = [ [0]*column for _ in range(numRows) ]        
        index_dict = {}
        
        for w in range(column):
            for h in range(numRows):
                index = 2*w + h
                q = index // N
                r = index % N
                
                if index >= LENGTH:
                    continue
                
                if index not in index_dict.keys():
                    index_dict[index] = 1
                    
                    if r < numRows:
                        h_index = r
                        w_index = (numRows-1)*q
                        if h_index >= numRows or w_index >= column:
                                continue
                        # print(f"(h, w): ({h_index}, {w_index}), index: {index}, s[index]: {s[index]}")
                        zero_matrix[h_index][w_index] = s[index]
                    
                    else: # r >= numRows
                        h_index = N - r
                        w_index = (numRows-1)*q + r - (numRows - 1)
                        if h_index >= numRows or w_index >= column:
                            continue
                        # print(f"(h, w): ({h_index}, {w_index}), index: {index}, s[index]: {s[index]}")
                        zero_matrix[h_index][w_index] = s[index]
                else:
                    continue
                
        # for c in zero_matrix:
        #     print(c)
                       
        answer = ""
        for z in zero_matrix:
            for zz in z:
                if zz == 0:
                    continue
                else:
                    answer += zz
                    
        # print(answer)
        
        return answer
    
print(Solution().convert("A", 1))

print(Solution().convert("PAYPALISHIRING", 3))
    
print(Solution().convert("PAYPALISHIRING", 4))

# print(Solution().convert("PAYPALISHIRING", 5))

# print(Solution().convert("PAYPALISHIRING", 9))

# print(Solution().convert("ABCDEF", 3))

# text = "Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers."

# print(Solution().convert(text, 10)) 

# text2 = "vaaikwgylgayymxymqiqlptbojyycxbyzdijbpimvknvykvkada"

# print(Solution().convert(text2, 10)) 