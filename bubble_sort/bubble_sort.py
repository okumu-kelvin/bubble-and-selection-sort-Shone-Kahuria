numbers = [5, 4, 3, 2, 1, 0]

def bubble_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    return unsorted_list  
sorted_numbers = bubble_sort(numbers)
print(sorted_numbers)
