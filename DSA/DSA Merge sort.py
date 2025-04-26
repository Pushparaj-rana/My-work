def merge_sort(elements):
    if len(elements) <= 1:
        return elements

    mid_point = len(elements)//2

    left = elements[:mid_point]
    right = elements[mid_point:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_list(left,right)

def merge_two_sorted_list(left,right):
    sorted_list = []

    len_left = len(left)
    len_right = len(right)
    i=j=0

    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    while i < len_left:
        sorted_list.append(left[i])
        i += 1

    while j < len_right:
        sorted_list.append(right[j])
        j += 1

    return sorted_list

if __name__ == '__main__':
    arr = [10,3,15,7,8,23,98,29]

    print(merge_sort(arr))
