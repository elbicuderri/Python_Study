class Solution:  ## not completed
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or len(s) <= numRows:
            return s
        if numRows == 1:
            return s
        
        N = 2*numRows-2
        # 3 -> 4
        # 4 -> 6
        # 5 -> 8
        
        LENGTH = len(s) # L == 14  , row == 3 ---> (3, 7) # L == 14 , row == 3 ---> (4, 7)
        print(LENGTH) 
        
        column = (numRows-1)*(LENGTH // N)
        
        if LENGTH%numRows == 0:
            column += 1
        
        if LENGTH%N == 0:
            column += 0
        elif LENGTH%N > 0 and LENGTH%N <= numRows:
            column += LENGTH%numRows
        else:
            column += LENGTH%numRows + 1
            
        print(numRows, column)
        
        zero_matrix = [ [0]*column for _ in range(numRows) ]
                                
        index_list = [ _ for _ in range(LENGTH) ]
        zero_list = [ 0 for _ in range(LENGTH)]
        index_dict = dict(zip(index_list, zero_list))
        
        for w in range(column):
            for h in range(numRows):
                index = 2*w + h
                q = index // N
                r = index % N
                
                if index >= LENGTH:
                    continue
                
                if index_dict[index] == 0:
                    index_dict[index] = 1
                    
                    if r < numRows:
                        h_index = r
                        w_index = (numRows-1)*q
                        if h_index >= numRows or w_index >= column:
                                continue
                        print(f"(h, w): ({h_index}, {w_index}), index: {index}, s[index]: {s[index]}")
                        # print(f"h: {h_index}, w: {w_index}, index: {index}, s[index]: {s[index]}")
                        zero_matrix[h_index][w_index] = s[index]
                    
                    else: # r >= numRows
                        h_index = N - r
                        w_index = (numRows-1)*q + r - (numRows - 1)
                        if h_index >= numRows or w_index >= column:
                            continue
                        print(f"(h, w): ({h_index}, {w_index}), index: {index}, s[index]: {s[index]}")
                        # print(f"h: {h_index}, w: {w_index}, index: {index}, s[index]: {s[index]}")
                        zero_matrix[h_index][w_index] = s[index]
                         
                else:
                    continue
                
        for c in zero_matrix:
            print(c)
                       
        answer = []
        
        for z in zero_matrix:
            for zz in z:
                if zz == 0:
                    continue
                else:
                    answer.append(zz)
                    
        # print(answer)
    
        return ''.join(answer)
    
    
#case1 = "PAYPALISHIRING", 3
#case2 = "PAYPALISHIRING", 4
#case3 = "A", 1

print(Solution().convert("A", 1))

print(Solution().convert("PAYPALISHIRING", 3))
    
print(Solution().convert("PAYPALISHIRING", 4))

print(Solution().convert("PAYPALISHIRING", 5))

print(Solution().convert("PAYPALISHIRING", 9))

print(Solution().convert("ABCDEF", 3))

text = "Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers."

print(Solution().convert(text, 10)) # not solved

print(len(text))
