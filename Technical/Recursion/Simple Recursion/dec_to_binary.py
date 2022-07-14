# ------------------------------------
# palindrome.py
#
# Determines if a string given at run time is a palindrome
# ------------------------------------
import sys

def main():
    results = ""

    if(len(sys.argv) > 1 and sys.argv[1].isdigit()):
        results = convertToBinary(int(sys.argv[1]), results)
        print("[SUCCESS] " + sys.argv[1] + " in binary is " + results)
    else:
        print("Please supply a number to convert")


def convertToBinary(decimal, results):
    if(decimal == 0):
        return results
    
    results = str(decimal%2) + results
    
    return convertToBinary(decimal//2, results)

if __name__ == '__main__':
    main()