def merge_sort(elements, key = None, descending = False ):
    if len(elements) <= 1:
        return elements

    mid_point = len(elements)//2

    left = elements[:mid_point]
    right = elements[mid_point:]

    left = merge_sort(left,key, descending=False)
    right = merge_sort(right,key, descending=False)

    #merge_two_sorted_list(left,right,key)

    if descending :
        sorted_elements = merge_two_sorted_list(left,right,key)
        len_sorted_elements = len(sorted_elements)
        descending_list = []
        for i in range(len(sorted_elements)):
            descending_list.append(sorted_elements[len_sorted_elements - i -1])
        return descending_list
    else:
        return merge_two_sorted_list(left,right,key)



def merge_two_sorted_list(left,right,key):
    sorted_list = []

    len_left = len(left)
    len_right = len(right)
    i=j=0

    while i < len_left and j < len_right:
        if left[i][key] <= right[j][key]:
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
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
    print(merge_sort(elements, key = 'time_hours', descending=True))

