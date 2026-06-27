# def gcd(n,m):
#     gcd=1
#     for i in range(1,min(n,m)+1):
#         if n%i==0 and m%i==0:
#             gcd=i
            
#     print(gcd)
    
    
# gcd(41,20)

def gcd(n,m):
    while n>0 and m>0:
        if n>m:
            n=n%m
        else:
            m=m%n
    if n==0:
       print(m)
    else:
        print(n)
            
gcd(20,15)
        
