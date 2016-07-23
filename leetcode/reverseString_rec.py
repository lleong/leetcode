#!/user/bin/python

def main():
    print reverseString_rec("hello")

'''
This function reverse a string using recusive
'''

def reverseString_rec(s):
    if not s:
       return s
    return s[-1] + reverseString_rec(s[:-1])

if __name__ == '__main__':
    main()
