#!/user/bin/python

def main():
    print reverseString("hello")

def reverseString(s):
    try:
        type(s) is str
        return s[::-1]
    except TypeError:
        print "input must be string"

if __name__ == '__main__':
    main()
