# ------------------------------------
# palindrome.py
#
# Determines if a string given at run time is a palindrome
# ------------------------------------
import sys

def main():
    if(len(sys.argv) > 1):
        checkIfPalindrome(sys.argv[1])
    else:
        print("Please supply a string to evaluate")


def checkIfPalindrome(input):
    lastChar = input[len(input) - 1]

    if(len(input) < 2):
        print("[SUCCESS] The supplied string is a palindrome")
    elif(input[0] == lastChar):
        checkIfPalindrome(input[1:lastChar])
    else:
        print("[ERROR] The supplied string is not a palindrome")

if __name__ == '__main__':
    main()