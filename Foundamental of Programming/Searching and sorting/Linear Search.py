#How It Works:-----
#Start from the first element of the list.
#compare it with the target value.
#If they are equal → ✅ return the index (position).
#If not → move to the next element.
#Keep doing this until you either:
#Find the target → return its index.
#Reach the end without finding it → return -1.





def linear_search(arr,target):
    size=len(arr)
    for index in range(0,size):
        if(arr[index]==target):
            return index
    
    return -1

my_list=[10,20,30,70,11]
target=20

result=linear_search(my_list,target)

print(result) 