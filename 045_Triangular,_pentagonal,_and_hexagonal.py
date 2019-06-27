'''Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	  T(n) = n(n+1)/2	 	  1, 3, 6 , 10, 15, ...
Pentagonal	 	P(n) = n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	  H(n) = n(2n−1)	 	  1, 6, 15, 28, 45, ...
It can be verified that T(285) = P(165) = H(143) = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
Link: https://projecteuler.net/problem=45'''

#Imports
import time

#Build a Triangle function
def Tri(n):
    return (n * ((3 * n) - 1)) / 2
    
#Build an isPentagonal function
#Note: this was derived by using the quadratic
#formula on the initial equation, (n(3n - 1)) / 2
#and getting a = 3/2, b = -1/2, and c = -n
def isPen(n):
    ans = (0.5 + (0.25 + (6 * n))**0.5) / 3
    return ans == int(ans)
    
#Build an isHexagonal function
#Note: this is also derived using the quadratic formula
def isHex(n):
    ans = (1 + (1 + (8 * n))**0.5) / 4
    return ans == int(ans)

#Build a solve function
def solve():
    #Define variables
    start = time.time()
    ans   = 0
    i     = 286
    while 1:
        num = Tri(i)
        if isPen(num) and isHex(num):
            ans = str(num)
            i   = str(i)
            break
        i += 1
    
    #Print the results
    print 'The next triangle number after T(285) = 40755 that is also '
    print 'pentagonal and hexagonal is T(' + i + ') = ' + ans + '.'
    print 'This took ' + str(time.time() - start) + ' seconds to calculate.'

#Run the program
solve()
