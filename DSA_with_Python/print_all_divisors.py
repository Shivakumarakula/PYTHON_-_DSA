# def divisors(n):
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i)
            
            
# divisors(36)



# or.............



def divisors(n):
    l=[]
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            # print(i)
            l.append(i)
            if n//i!=i:
                # print(n//i)
                l.append(n//i)
            
    print(sorted(l))
divisors(36)


