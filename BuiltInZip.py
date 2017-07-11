import itertools
def Main():
    if False:
        # basic operations #
        list1 = [1,2,3,4,5,6]
        list2 = ['a','b','c','v','r','y']
        zipped = zip(list1, list2)
        for i, j in zipped:
            print(str(i) + '+' + str(j))
    if True:
        # zip: add line number file #
        with open('a.txt') as inputFile:
            for i, j in zip(itertools.count(1), inputFile):
                print(str(i) + ': ' + j[:-1])


if __name__ == '__main__':
    Main()
