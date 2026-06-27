
#selection sort...
def selection_sort(arr,n):
    for i  in range(n-1):
        min=i
        for j in range(i,n,1):
            if arr[j]<arr[min]:
                min=j
        arr[min],arr[i]=arr[i],arr[min]
        print("runs..")
    
    
    

#bubble sort.....
def bubble_sort(arr, n):
    
    for i in range(n-1,0,-1):
        swapcount=0
        for j in range(0,i,1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapcount+=1
        if swapcount==0:
            break
        print("runs...")
    


#recursive buble sort....
def recursive_bubblesort(arr, n):
    if n==1:
        return
    swapcount=0
    for j in range(n-1):
        
        if arr[j] > arr[j + 1]:
            # Swap elements
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swapcount+=1
    if swapcount==0:
        return
    recursive_bubblesort(arr, n - 1)


#insertion sort....
def insertion_sort(arr,n):
    for i in range(n):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1], arr[j]=arr[j],arr[j-1]
            j-=1
            
            print("runs...")



def recursive_insertion_sort(arr, i, n):
    # Base case
    if i == n:
        return

    j = i
    # Move the element to the left while it's smaller than its predecessor
    while j > 0 and arr[j - 1] > arr[j]:
        # Swap
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
        j -= 1

    # Recur for the next index
    recursive_insertion_sort(arr, i + 1, n)





#merge sort....
def merge(arr,low, mid, high):
    temp=[]
    left=low
    right=mid+1
    
    while left<=mid and right<=high:
        if arr[left]<=arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    
    while(left<=mid):
        temp.append(arr[left])
        left+=1
    while(right<=high):
        temp.append(arr[right])
        right+=1
        
    # copy back to original array
    for i in range(low, high+1):
        arr[i] = temp[i-low]

def merge_sort(arr, low, high):
    if low>=high:
        return
    else:
        mid=(low+high)//2
        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1,high)
        merge(arr, low, mid, high)
    







#quick sort....
def partition(arr, low, high):
    pivot=arr[low]
    i=low
    j=high
    while(i<j):
        while arr[i]<=pivot and i<=high:
            i+=1
        while arr[j]>pivot and j>=low:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]
    
    arr[low],arr[j]=arr[j],arr[low]
    return j



def quicksort(arr, low, high):
    if low<high:
        partition_index=partition(arr,low,high)
        quicksort(arr, low, partition_index-1)
        quicksort(arr,partition_index+1,high)
    
    







arr=[1,2,7,8,9,4,5]
n=len(arr)
print(arr)
# selection_sort(arr,n)
# bubble_sort(arr, n)
# insertion_sort(arr, n)
# merge_sort(arr, 0, n-1)
# pivot=arr[0]
# quicksort(arr, 0, n-1 )

# recursive_bubblesort(arr,n)
# recursive_insertion_sort(arr,0,n)
print(arr)





