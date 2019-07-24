import numpy as np

def ktom(ke):
    k = []
    ma = [0]*26
    for  i in ke:
        k.append(i)
    
    ans= []    
    for i in ke:
        if i not in ans:
            ans.append(i)
        
    for i in k:
       ma[ord(i)-97] = ma[ord(i)-97] + 1
       
    for i in ma:
        if i>=2:
            i = 1
    
    for i in range(26):
        if ma[i] == 0:
            x = chr(i+97)
            if 'i' in ans:
                if i == 9:
                    continue
            
            if 'j' in ans:
                if i == 8:
                    continue
            
            if x not in ans:
                ans.append(x)
                
    final1 =  np.array(ans)
    
    fmat =  final1.reshape(5,5)
    
    return fmat
def position(matrix,val):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == val:
                return i,j


ke = input()
matrix = ktom(ke)
      
        

