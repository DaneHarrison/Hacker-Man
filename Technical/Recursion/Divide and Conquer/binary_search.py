import sys
entries = [1, 3, 5, 7, 9]

def main():
    if(len(sys.argv) > 1 and sys.argv[1].isdigit()):
        results = binarySearch(entries, 0, len(entries) - 1, int(sys.argv[1]))
        
        if(results == -1):
            print("[ERROR] could not locate " + sys.argv[1])
        else:
            print("[SUCCESS] found " + sys.argv[1] + " in position " + str(results))
    else:
        print("Please supply a number to search for")


def binarySearch(entries, left, right, searchVal):
    mid = (left + right)//2

    if(left > right):
        return -1
    elif(entries[mid] == searchVal):
        return mid + 1
    elif(entries[mid] > searchVal):
        return binarySearch(entries, left, mid - 1, searchVal)
    else:
        return binarySearch(entries, mid + 1, right, searchVal)

if __name__ == '__main__':
    main()