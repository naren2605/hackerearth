T=int(input())
for ti in range(1,T+1):
    n=int(input())
    index=0
    sum1=0
    sum2=0
    for i in input().strip().split(' '):
        i=int(i)
        if index%2==0:
            sum1=sum1+i
        else:
            sum2=sum2+i
        index=index+1
    print(sum1,sum2)
"""    
    if sum1<sum2:
        print("Case "+str(ti)+":",sum2)
    else:
        print("Case "+str(ti)+":",sum1)
"""
