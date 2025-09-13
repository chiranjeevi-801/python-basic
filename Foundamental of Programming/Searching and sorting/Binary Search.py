## print(5//2)

def binary_search(arr,target):
    size=len(arr)-1

    start=0
    end=size-1

    while(start<= end):
        mid=(start+end)//2

        if ( arr[mid]==target):
            return mid # found the target
        
        elif(arr[mid]>target):
            end=mid-1
        
        elif(arr[mid]<target):
            start=mid+1
    return-1

sorted_list=[10,23,35,45,50,70,85]
target=23

result=binary_search(sorted_list,target)
print(result)


#------------------------------------------------------------------------------------------------
## EXAMPLE 01:-

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2  # Find middle index
        if arr[mid] == target:
            return mid  # Found, return position
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half

    return -1  # Not found

# Example usage:
numbers = [2, 4, 6, 8, 10, 12, 14]
target = 10

result = binary_search(numbers, target)

if result != -1:
    print(f"Found {target} at index {result}")
else:
    print(f"{target} not found in the list")

