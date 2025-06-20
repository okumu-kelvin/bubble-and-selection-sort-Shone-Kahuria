numbers= [5, 4, 3, 2, 1, 0]

def selection_sort(unsorted_list):
    n= len(unsorted_list)
    for i in range(n):
        min_idx= i
        for j in range(i + 1, n):
            if unsorted_list[j] < unsorted_list[min_idx]:
                min_idx = j
        unsorted_list[i], unsorted_list[min_idx] = unsorted_list[min_idx], unsorted_list[i]
    return unsorted_list

sorted_numbers = selection_sort(numbers)
print(sorted_numbers)