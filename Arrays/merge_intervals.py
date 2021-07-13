def merge_intervals(n):
    merged = []
    n.sort(key=lambda x:x[0])
    print(n)

    """ basically, check if merged is empty or the last item in the merged list is less than the first item of the next element
    if yes, then append it to the merged list. 
    Else - if we already have an element in merged list, then simply merge the last item with the max of the (last_item in merged list,last item in the next list
    
    O(nlogn) time complexity as we are traversing the list once and sorting it first based on the first elements & O(n) space as we have a merged list that we append elements to
    """

    for i in n:
        if not merged or merged[-1][-1]<i[0]:
            merged.append(i)
        else:
            merged[-1][-1] = max(merged[-1][-1],i[-1])
    return merged



print(merge_intervals([[1,4],[4,5]]))
print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))