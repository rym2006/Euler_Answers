'''Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, 
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
Link: https://projecteuler.net/problem=2'''

#Imports
import time

#Sum of even fibonacci numbers function
def EvenFibSum(n):
    #Define variables
    start = time.time()
    fib = [1, 2]
    
    #Solve the problem
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    
    ans = str(sum(fib[i] for i in range(1, len(fib), 3)))
    n = str(n)
        
    #Print the results
    print('The sum of the even-valued terms in the Fibonacci ')
    print('sequence below ' + n + ' is ' + ans + '.')
    print('This took ' + str(time.time() - start) + ' seconds to calculate.')

#Run the program
n = 4000000
EvenFibSum(n)
