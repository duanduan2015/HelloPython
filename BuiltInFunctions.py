import itertools
def Main():
    if False:
        # basic operations #
        list1 = [1,2,3,4,5,6]
        list2 = ['a','b','c','v','r','y']
        zipped = zip(list1, list2)
        for i, j in zipped:
            print(str(i) + '+' + str(j))
    if False:
        # zip: add line number file #
        with open('a.txt') as inputFile:
            for i, j in zip(itertools.count(1), inputFile):
                print(str(i) + ': ' + j[:-1])
    if False:
        # bin() conver int to binary
        class Number:
            def __init__(self, string):
                self.string = string 
            def __index__(self):
                return int(self.string)
        n1 = Number('1111')
        n2 = 1111
        print('Number object binary rep. is: ' + ascii(bin(n1)))
        print('number 1111   binary rep. is: ' + ascii(bin(n2)))

    if False:
        print('bool(1) is: ' + ascii(bool(1)))
        print('bool(-1) is: ' + ascii(bool(-1)))
        print('bool(0) is: ' + ascii(bool(0)))
        print('bool(True) is: ' + ascii(bool(True)))
        print('bool(False) is: ' + ascii(bool(False)))

    if False:
        a = [1,2,3,4]
        print('bytearray of [1,2,3,4] is mutable' + ascii(bytearray(a)))
        print('bytes of [1,2,3,4] is immutable' + ascii(bytes(a)))

    if True:
        a = [1,2,3,4,5,6]
        print(a)
        print('reversed(a) is: ')
        for i in reversed(a):
            print(i)



if __name__ == '__main__':
    Main()
