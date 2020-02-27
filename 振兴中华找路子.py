def f(x,y):
    
    if(x==3 or y==4):
        return True
    return f(x+1,y)+f(x,y+1)
d=f(0,0)
print(f(0,0))
