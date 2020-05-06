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
    return quick_sort(smaller_sequence) + [pivot] + quick_sort(greater_sequence)

print(quick_sort([1,4,2,6,3,5,7]))