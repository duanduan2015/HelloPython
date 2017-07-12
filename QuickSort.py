import sys

def quickSort(list1, start, end):
    if start == end or start == end - 1:
        return
    pivot = list1[start]
    pivotIndex = start
    index = start + 1
    while index < end:
        if pivot > list1[index]:
            if index - 1 > pivotIndex:
                list1[pivotIndex] = list1[index]
                list1[index] = list1[pivotIndex + 1]
                list1[pivotIndex + 1] = pivot
                pivotIndex += 1
            else:
                list1[pivotIndex] = list1[index]
                list1[index] = pivot
                pivotIndex = index
        index += 1
    quickSort(list1, start, pivotIndex)
    quickSort(list1, pivotIndex + 1, end)
    

def Main():
    list1 = []
    for i in sys.argv[1].split():
        list1.append(int(i))
    quickSort(list1, 0, len(list1)) 
    print(list1)
if __name__=='__main__':
    Main()
