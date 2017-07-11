def Main():
    with open('a.txt') as inputFile, open('b.txt', 'w') as outputFile:
        for line in inputFile:
            print(int(line) + 1, file=outputFile)
            

if __name__ == '__main__':
    Main()

