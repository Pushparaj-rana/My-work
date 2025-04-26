def bubble_sort(elements):
    size = len(elements)

    for i in range(size - 1):

        swapped = False
        for j in range(size-1-i):
            if elements[j] > elements[j+1]:

                tmp = elements[j]
                elements[j] = elements[j+1]
                elements[j+1] = tmp
                swapped = True
        if not swapped:
            break



if __name__ == "__main__":
    #elements = [23,12,5,46,27,55,82,1]
    #elements = [1,2,3,4,2]
    elements = ["mona", "dhaval", "aamir", "tina", "chang"]
    bubble_sort(elements)
    print(elements)

