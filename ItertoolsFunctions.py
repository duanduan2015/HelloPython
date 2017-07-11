import itertools
def Main():
    list1 = [1,2,3,4,5]
    list2 = ['a','b','c','d','e','r','f']
    for i, j in itertools.product(list1, list2):
        print(str(i) + j)

if __name__ == '__main__':
    Main()
