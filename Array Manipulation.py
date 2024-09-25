
def arrayManipulation(n, queries):
    # Write your code here
    arr=[0] * n
    for query in (queries):
        start=query[0]
        end=query[1]
        added=query[2]
        if end< len(arr):
            arr[end] -=added
            arr[start-1] +=added
        else:
            arr[start-1] += added
    prefix=0
    for i in range(len(arr)):
        prefix += arr[i]
        arr[i]=prefix
    return max(arr)
