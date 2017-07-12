import sys

def merge(left, right):
    sortedList = []
    leftIndex = 0 
    rightIndex = 0 
    if left == None:
        return right
    if right == None:
        return left
    while leftIndex < len(left) and rightIndex < len(right):
        if left[leftIndex] <= right[rightIndex]:
            sortedList.append(left[leftIndex])
            leftIndex += 1
        else:
            sortedList.append(right[rightIndex])
            rightIndex += 1
    if leftIndex < len(left):
        sortedList.extend(left[leftIndex:])
    if rightIndex < len(right):
        sortedList.extend(right[rightIndex:])
    return sortedList

def MergeSort(list1):
    if list1 == None or len(list1) == 1:
        return list1
    mid = len(list1) // 2
    listA = MergeSort(list1[:mid])
    listB = MergeSort(list1[mid:])
    return merge(listA, listB)


def Main():
    list1 = []
    for i in sys.argv[1].split():
        list1.append(int(i))
    result = MergeSort(list1) 
    print(result)

if __name__=='__main__':
    Main()
