def perfectSquare():
    n=int(input("enter the size: "))
    list=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        list.append(l)
    
    m=int(n/2)
    m1=int(n-1)
    # list[m][m1]=1
    
    num=1
    while(num<=n*n):
       
        if(m==-1 and m1==n):
            m=0
            m1=n-2
        else:
            if(m==-1):
                m=n-1
            if(m1==n):
                m1=0
    
        if(list[m][m1]!=0):
            m=m+1
            m1=m1-2
            continue
        else:
            list[m][m1]=num
            #print(num)
            num=num+1
        
        #num=num+1
        m=m-1
        m1=m1+1
    
    display(list,n)
    
def display(list,n):
    for i in range(n):
        for j in range(n):
            print(list[i][j],end=" ")
        print("\n")
        
perfectSquare()
            
            
            
            
            