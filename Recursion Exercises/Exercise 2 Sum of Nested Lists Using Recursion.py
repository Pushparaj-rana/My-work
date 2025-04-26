def sum_of_nested_list(nested_list):
   total = 0
   for list1 in nested_list:

       if type(list1) == type([]):
           total = total + sum_of_nested_list(list1)
       else:
           total = total + list1
   return total
           
           


'''def sum_of_nested_list(nested_list):
    total = 0
    for element in nested_list:
        if isinstance(element, list):  # Check if the element is a nested list
            total += sum_of_nested_list(element)  # Recursively sum nested lists
        elif isinstance(element, (int, float)):  # Check if the element is a number
            total += element
    return total

'''
    

if  __name__ == '__main__':
    arr = [2,[3,4],[6,8],[1,3,[2,11]]]
    print(sum_of_nested_list(arr))
    
    
     
