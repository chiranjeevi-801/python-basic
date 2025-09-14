def bubble_sort(lst):
    n = len(lst)
    # Traverse through all elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


# Example usage:
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))  # Output: [11, 12, 22, 25, 34, 64, 90]

print(bubble_sort([12,25,11,34,90,22]))               # Output: [1, 2, 4, 5, 8]
