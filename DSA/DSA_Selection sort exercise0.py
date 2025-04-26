def selection_sort(arr,key1,key2):
    size =  len(arr)
    for i in range(size - 1):
        min_value_index = i
        for j in range(min_value_index + 1,size):
            if arr[j][key1] < arr[min_value_index][key1]:
                min_value_index = j
        if i!= min_value_index:        
            arr[i], arr[min_value_index] = arr[min_value_index], arr[i]

    for k in range(size -1):
        min_index = k
        for a in range(min_index + 1,size):
            if arr[a][key1] == arr[min_index][key1]:
                if arr[a][key2] < arr[min_index][key2]:
                    min_index = a
        arr[k], arr[min_index] = arr[min_index], arr[k]










if __name__ == '__main__':
    print("Main block is running!")
    arr = [{'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}]


    selection_sort(arr,'First Name','Last Name')
    print(f"{arr}")

    selection_sort(arr,'Last Name','First Name')
    print(f"{arr}")
    