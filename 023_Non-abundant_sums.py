'''A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 
28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant 
if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as 
the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater 
than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any 
further by analysis even though it is known that the greatest 
number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
Link: https://projecteuler.net/problem=23'''

#Imports
import time

#Build an is Abundant function
def isAbundant(n):
    pd = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            pd.append(i)
            pd.append(n // i)
    return sum(set(pd)) > n

#Solution function
def solve():
    #Declare variables
    start = time.time()
    num = 28123
    abundants = [i for i in range(1, num + 1) if isAbundant(i)]
    nums = [0] * (num + 1)
    
    #Solve the problem
    for i in abundants:
        for j in abundants:
            if i + j <= num:
                nums[i + j] = 1
                
    total = str(sum(i for i in range(1, num + 1) if nums[i] == 0))
    
    #Print the results
    print('The sum of all the positive integers which cannot be ')
    print('written as the sum of two abundant numbers is ' + total + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
solve()
