def printName(n, name):
    if n!=0:
        print(name)
        n-=1
        printName(n,name)
    else:
        return
    
    

# printName(5,'shiva')


# def printInverse(n):
#     if n<1:
#         return
#     print(n)
#     n-=1
#     printInverse(n)

# printInverse(6)



def printInverse(i,n):
    if i>n:
        return
    printInverse(i+1,n)
    print(i)
    

# printInverse(1,5)


def sum(n):
    if n==1:
        return 1
    return n+sum(n-1)
    
# print(sum(10))

def fact(n):
    if n<=1:
        return 1
    return n*fact(n-1)


# print(fact(3))
l=[1,2,3,4,5,9]
# i=0
n=len(l)
def reversearr(i):
    if l[i]>=n//2:
        return
    l[i],l[n-i-1]=l[n-i-1],l[i]
    reversearr(i+1)
    



# print("Array= ",l)

# reversearr(0)

# print("Array= ",l)


s="madam"
n-len(s)
def check_str_pdrm(i):
    if i>= n//2:
        return True
    if s[i]==s[n-i-1]:
        return check_str_pdrm(i+1)
    
# check_str_pdrm(0)
