'''
Problem:
Given a non-negative interger, 
add all its digits util the result has only one digit.
eg: num = 49 => 4+9 = 13 => 1+ 3 = 4 return 4
'''  

'''
Solution 1
Using mod and divder to sum up all the digit
return value utill it is smaller then 10
'''
def addDigits(num):
   while num >= 10:
       num = helper(num)
   return num


def helper(num):
    if num < 10:
        return num
    return num%10 + helper(num/10)


'''
Solution 2
We can just mod the number by 9
Since the range answer is between 1 to 9
if the number can mod by 9 we return 9
'''
def addDigits_2(num):
    if num % 9 == 0:
        return 9
    else:
        return num % 9

print addDigits(323)
print addDigits_2(323)
