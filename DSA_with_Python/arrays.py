
# 1. find the largest number an arry....2 approchs --> 1. first  sort arry using quick/mege/any sort and return arr[n-1] so by this TC=O(nlogn) and 2nd apporch is ---> using loop then TC=O(n) much lesser than O(nlogn)
def largestElement(nums):
    large=nums[0]
    for i in nums:
        if i>large:
            large=i
    return large
    
    
arr=[-4,-3,0,1,-8]
# print(largestElement(arr))



#2 finding the second largest number...or #3 finding the second smallest number.
# it have solutions:
# 1st bruteforce.. is by sorting then finding second second largest number by the compare again back to array element from n-1 to 0 with larget number(n-1 index) because their is a change of get larger number 2 time or more time in the array ex: 1,2,3,4,5,5,5 so here arr[n-2] is not second large. TC=O(nlogn)sorting+o(n)for again checking.
# 2nd apporch is... first find larget number them using largest number compare with the array again to get lesser than the largest number so by this TC=O(n)for largest number + O(n) for checking..total TC=O(2n)


#3rd apporch is below with single loop and TC=O(n)

def second_largestnumber(arr):
    first=arr[0]
    second=-1
    
    for i in arr:
        if i>first:
            second=first
            first=i
        elif i<first and i>second:
            second=i
    return second


def second_smallestnumber(arr):
    smallest=arr[0]
    second_smallest=float('inf')
    
    for i in arr:
        if i<smallest:
            second_smallest=smallest
            smallest=i
        elif i!=smallest and i<second_smallest:
            second_smallest=i
    return second_smallest

arr=[10,2,5,3,1,8,0]
# print(second_largestnumber(arr))
# print(second_smallestnumber(arr))




#4 check wheather arry is sorted or not...
def checkarr_sort(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True



arr=[1,2,3,4,5,6]
print(checkarr_sort(arr))







