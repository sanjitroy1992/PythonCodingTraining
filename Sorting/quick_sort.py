"""
Time complexity:
O(nlogn) -> Best & Average Case
O(n**2) -> Worst Case
"""


def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    smaller_sequence = []
    greater_sequence = []
    for item in sequence:
        if item > pivot:
            greater_sequence.append(item)
        else:
            smaller_sequence.append(item)
    print([pivot])
    return quick_sort(smaller_sequence) + [pivot] + quick_sort(greater_sequence)

print(quick_sort([9,1,4,2,6,3,5,7,10]))