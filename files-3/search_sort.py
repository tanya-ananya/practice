#!/usr/bin/env python
# coding: utf-8

# In[1]:


def LinearSearch(number, key):
    for i in range(len(number)):
        if number[i] == key:
            return i
    return -1
    
number = [14, 18, 52, 10, 0, 1, 3, 8, 19, 34]

key = 99

result = LinearSearch(number, key)

if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)
    


# In[2]:


def binarySearch(number, key, low, high):

    if high >= low:

        mid = low + (high - low)//2

        if number[mid] == key:
            return mid


        elif number[mid] > key:
            return binarySearch(number, key, low, mid-1)


        else:
            return binarySearch(number, key, mid + 1, high)

    else:
        return -1


number = [0, 1, 3, 8, 14, 18, 19, 34, 52]
key= 99

result = binarySearch(number, key, 0, len(number)-1)

if result != -1:
    print("Element is found at index " + str(result))
else:
    print("Not found")


# In[3]:


def BubbleSort(arr):
    n=len(arr)
    
    if n<=1:
        return arr
    
    for i in range (n):
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                
                (arr[j],arr[j+1])=(arr[j+1],arr[j])
    return arr


arr = [14,46,43,27,57,41,45,21,70]
bubblesort = BubbleSort(arr)
print("The unsorted list is", arr)
print("The Bubble sorted list is", bubblesort)


# In[11]:


def SelectionSort(arr):
    n=len(arr)
    
    if n<=1:
        return arr
    
    for i in range(0,n-1):
        
        minIndex=i
        
        for j in range(i+1,n):          
            if arr[j] < arr[minIndex]:
                minIndex=j
                
        if minIndex!=i:                     
            (arr[minIndex],arr[i])=(arr[i],arr[minIndex])
    return arr
 
arr = [14,46,43,27,57,41,45,21,70]
selectsort = SelectionSort(arr)
print("The unsorted list is", arr)
print("The Selection sorted list is", selectsort)


# In[12]:


def InsertSort(arr):
    n=len(arr)
    
    if n<=1:
        return arr
    
    for i in range(1,n):
        j=i
        target=arr[i]   
        
        while j > 0 and target < arr[j-1]:       
            arr[j]=arr[j-1]
            j=j-1
            
        arr[j]=target            
    return arr

arr = [14,46,43,27,57,41,45,21,70]
insertsort = InsertSort(arr)
print("The unsorted list is", arr)
print("The Selection sorted list is", insertsort)


# In[13]:


def mergeSort(nlist):
    print("Splitting ",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",nlist)

nlist = [14,46,43,27,57,41,45,21,70]
print("The unsorted list is", arr)
print("The Merge sorted list is", mergeSort(nlist))


# In[42]:


# Quick sort in Python

# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
    pivot = array[high]

  # pointer for greater element
    i = low - 1

  # traverse through all elements
  # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
          i = i + 1

      # swapping element at i with element at j
          (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
    return i + 1

# function to perform quicksort
def quickSort(array, low, high):
    if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
        pi = partition(array, low, high)

    # recursive call on the left of pivot
        quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
        quickSort(array, pi + 1, high)


data = [14,46,43,27,57,41,45,21,70]
print("Unsorted Array", data)


size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:', data)


def binarySearch(number, key, low, high):

    if high >= low:

        mid = low + (high - low)//2

        if number[mid] == key:
            return mid


        elif number[mid] > key:
            return binarySearch(number, key, low, mid-1)


        else:
            return binarySearch(number, key, mid + 1, high)

    else:
        return -1

key = 41

result = binarySearch(data, key, 0, len(number)-1)

if result != -1:
    print("Element is found at index " + str(result))
else:
    print("Element is not found")


# In[ ]:




