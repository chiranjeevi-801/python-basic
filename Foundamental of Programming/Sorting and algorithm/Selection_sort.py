
## EXAMPLE :--


def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        # Assume the minimum is the first element of the unsorted part
        min_index = i
        # Find the minimum element in the remaining unsorted part
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        # Swap the found minimum with the first element of the unsorted part
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


# Example usage:
print(selection_sort([64, 25, 12, 22, 11]))  # Output: [11, 12, 22, 25, 64]
print(selection_sort([29, 10, 14, 37, 13]))  # Output: [10, 13, 14, 29, 37]


                                               ## OR


def selection_sort(arr):
    n=len(arr)
    min_index=0

    for i in range (n-1):
        min_index=0 

        for j in range(1,n):
            if(arr[j]<arr[min_index]):
                min_index=j
        arr[0],arr[min_index]=arr[min_index],arr[0]

    return arr
     
unsorted_list =[12,25,11,34,90,22]
sorted_list = selection_sort(unsorted_list)
print("sorted element:",sorted_list)

#https://visualgo.net/en/sorting    