for a in range(100000,1000000):
    b=str(a)
    if(b[0]!=b[1] and b[0]!=b[2] and b[0]!=b[3]and b[0]!=b[4]and b[0]!=b[5]and b[1]!=b[2]and b[1]!=b[3]and b[1]!=b[4]and b[1]!=b[5]and b[2]!=b[3]and b[2]!=b[4]and b[2]!=b[5]and b[3]!=b[4]and b[3]!=b[5]and b[4]!=b[5]):
        c=int(b)
        d=str(c*c)
        if(b[0] not in d and b[1] not in d and b[2] not in d and b[3] not in d and b[4] not in d and b[5] not in d):
            print(b)
        
    
