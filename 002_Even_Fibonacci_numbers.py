'''Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, 
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
Link: https://projecteuler.net/problem=2'''

#Imports
import time

#Build an Even Fibonacci Sum function
def efSum(n):
    fib = [1, 2]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    if fib[-1] >= n: fib = fib[:-1]
    return sum(fib[i] for i in range(1, len(fib), 3))

#Sum of even fibonacci numbers function
def solve(n):
    #Define variables
    start = time.time()
    
    #Solve the problem
    ans = str(efSum(n))
    n = str(n)
        
    #Print the results
    print('The sum of the even-valued terms in the Fibonacci ')
    print('sequence below ' + n + ' is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
n = 4 * 10**6
solve(n)
