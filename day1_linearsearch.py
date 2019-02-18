# Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[]. 

def search(element, array):
    for i in array:
        if element == i:
            return array.index(i)

index = search(eval(input()), eval(input()))
print(index)
