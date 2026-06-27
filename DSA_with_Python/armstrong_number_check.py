# def astrongNumber(n):
#     num=n
#     count=0
#     sum=0
#     digits=[]
#     while(n>0):
#         digits.append(n%10)
#         count+=1
#         n=n//10
        
#     for i in digits:
#         sum=sum+(i**count)
        
#     if(sum==num):
#         print("yes= ",num," ",sum)
#     else:
#         print("No ",num, " ", sum)
        

# astrongNumber(153)




# or.......................



def astrongNumber(n):
    num=n
    sum=0
    count=len(str(n))
    while(n>0):
        sum=sum+((n%10)**count)
        n=n//10
        
    if(sum==num):
        print("yes= ",num," ",sum)
    else:
        print("No ",num, " ", sum)
        

astrongNumber(15)