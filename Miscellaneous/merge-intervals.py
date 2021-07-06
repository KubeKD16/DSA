"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.



Constraints:

    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104


"""

def merge_intervals(s):
    """ Sort the list first with the first element in the list- which takes O(nlogn) time & then check the last item of a list with the first item of the next list,
    if less then merge it to merged[] list. Else find the max of the last item of the first list & last item of the second list and append them to merged[].

    Time complexity - O(nlogn) -- (nlogn + n {for the size of the list})
    Space Complexity - O(n) as we are adding a new merged list that will equal if not be equivalent to the length of the input
    """
    merged = []
    s.sort(key=lambda y:y[0])

    for x in s:
        if not merged or merged[-1][-1] < x[0]:
            merged.append(x)
        else:
            merged[-1][-1] = max(merged[-1][-1],x[-1])

    return merged





input = [[1,4],[4,5]]
input1 = [[1,3],[2,6],[8,10],[15,18]]
print(merge_intervals(input1))
