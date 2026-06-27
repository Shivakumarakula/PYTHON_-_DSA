def pattern1(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()
        
        

# pattern1(5)

def pattern2(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()
        

# pattern2(5)



def pattern3(n):
    for i in range(1,n+1,1):
        for i in range(1,i+1):
            print(i, end=" ")
        
        print()
        
        
# pattern3(5)


def pattern4(n):
    for i in range(1,n+1,1):
        for j in range(1,i+1,1):
            print(i, end=" ")
        print()
        
        
# pattern4(5)


def pattern5(n):
    for i in range(1,n+1):
        for j in range(0, n-i+1,1):
            print("*", end=" ")
        print()
        
# pattern5(5)
def pattern6(n):
    for i in range(1, n+1):
        for j in range(1, n-i+2,1):
            print(j, end=" ")
        print()
        
        
# pattern6(5)




def pattern7(n):
    for i in range(1,n+1,1):
        # space..
        for j in range(1,n-i+1):
            print(" ", end=" ")
        
        # star...
        for m in range(0,2*i-1,1):
            print("*", end=" ")
        
        # space...
        for j in range(1,n-i+1):
            print(" ", end=" ")
        print()
        
# pattern7(5)
    
    

def pattern8(n):
    for i in range(1,n+1,1):
        # space...
        for j in range(1,i):
            print(" ", end=" ")
        # star...
        for m in range(0,2*n-(2*i-1),1):
            print("*", end=" ")
        # space...
        for j in range(1,i):
            print(" ", end=" ")
        print()
        
# pattern8(5)

def pattern9(n):
    
    for i in range(1,n+1,1):
        # space..
        for j in range(1,n-i+1):
            print(" ", end=" ")
        
        # star...
        for m in range(0,2*i-1,1):
            print("*", end=" ")
        
        # space...
        for j in range(1,n-i+1):
            print(" ", end=" ")
        print()
    
    for i in range(1,n+1,1):
        # space...
        for j in range(1,i):
            print(" ", end=" ")
        # star...
        for m in range(0,2*n-(2*i-1),1):
            print("*", end=" ")
        # space...
        for j in range(1,i):
            print(" ", end=" ")
        print()
    
   
        
    
    
# pattern9(5)


def pattern10(n):
    for i in range(1,2*n,1):
        star=i;
        if(i>n):
            star=2*n-i
        for j in range(0,star,1):
            print("*", end=" ")
        print()
        
# pattern10(5)


def pattern11(n):
    start=1
    for i in range(1,n+1,1):
        
        if i%2==0:
            start=0
        else:
            start=1
        for j in range(1,i+1,1):
            print(start, end=" ")
            start=1-start
        print()
        
# pattern11(5)


def pattern12(n):
    space=2*(n-1)
    for i in range(1,n+1,1):
        # numbers..
        for j in range(1,i+1,1):
            print(j, end=" ")
        
        # space...
        for j in range(1,space+1,1):
            print(" ",end=" ")
        
        # numbers...
        for j in range(i,0,-1):
            print(j, end=" ")
        print()
        space-=2
        
# pattern12(4)


def pattern13(n):
    num=1
    for i in range(1,n+1,1):
        for j in range(1,i+1,1):
            print(num, end=" ")
            num+=1
        print()
        
# pattern13(5)


def pattern14(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65+j), end=" ")
        print()

# pattern14(5)
        
        
def pattern15(n):
    for i in range(n):
        for j in range(n-i):
            print(chr(65+j), end=" ")
        print()

# pattern15(5)


def pattern16(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65+i),end=" ")
        print()
        
# pattern16(5)


def pattern17(n):

    for i in range(1,n+1):
        
        # space..
        for j in range(1,n-i+1):
            print("*",end=" ")
        
        # letters..
        # breakpoint=(2*i+1)/2
        breakpoint=i
        ch='A'
        for j in range(1,2*i):
            print(ch, end=" ")
            if j< breakpoint:
                ch=chr(ord(ch) + 1)
                
            else:
                ch=chr(ord(ch)- 1)
                
        
        # space...
        for j in range(1,n-i+1):
            print("*", end=" ")
        print()
        
        
# pattern17(4)


def pattern18(n):
    for i in range(1,n+1,1):
        ch='A'
        for j in range(0, i):
            print(chr(ord(ch)+ n-i+j), end=" ")
        print()
        
# pattern18(5)


def pattern19(n):
    for i in range(n):
        #star..
        for j in range(1,n-i+1):
            print("*", end=" ")
        #space..
        for j in range(i*2):
            print(" ", end=" ")
        #star...
        for j in range(1,n-i+1):
            print("*", end=" ")
        print()
        
    
    for i in range(1,n+1):
        #star..
        for j in range(1,i+1):
            print("*", end=" ")
        #space..
        for j in range(2*(n-i)):
            print(" ", end=" ")
        #star...
        for j in range(1,i+1):
            print("*", end=" ")
        print()
        
# pattern19(5)


# def pattern20(n):
#     space= 2*n-2
#     for i in range(1,2*n):
#         if i<=n:
#              stars=i
#         else:
#              stars=2*n-i
#         # stars...
#         for j in range(0,stars):
#             print("*", end=" ")
        
#         #spaces..
#         for j in range(0,space):
#             print(" ",end=" ")
        
#         #stars...
#         for j in range(0, stars):
#             print("*", end=" ")
#         print()
#         if i<n:
#             space+=2
#         else:
#             space-=2
# pattern20(5)


def pattern20(n):
    space = 2 * n - 2  # or =0
    for i in range(1, 2 * n):
        if i <= n:
            stars = i
        else:
            stars = 2 * n - i
        # stars count on each side 
        # or = below statement
        # stars = i if i <= n else 2 * n - i

        # left stars
        for j in range(stars):
            print("*", end=" ")

        # spaces
        for j in range((2 * n - stars * 2)):
            print(" ", end=" ")

        # right stars
        for j in range(stars):
            print("*", end=" ")

        print()  # move to next line

# Example usage:
# pattern20(5)


def pattern21(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==1 or i==n or j==1 or j==n:
                print("*", end=" ")
            else:
                print(" ",end=" ")
        print()
        
# pattern21(4)


def pattern22(n):
    size = 2 * n - 1  # grid size
    for i in range(size):
        for j in range(size):
            # distance from each border
            top = i
            left = j
            bottom = size - 1 - i
            right = size - 1 - j

            # minimum distance to any border
            min_dist = min(top, left, bottom, right)

            # value = n - min_dist
            print(n - min_dist, end=" ")
        print()

# Example usage:
pattern22(4)
