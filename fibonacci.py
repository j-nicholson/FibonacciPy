""" Python Program for calculating the nth Fibonacci number
f[n] = f[n - 1] + f[n - 2] """

import time

""" Recursive Fib calcuation """
def fibonacciR(n):
    if n <= 2:
        return 1
    else:
        return fibonacciR(n - 1) + fibonacciR(n - 2)

""" Iterative Fib calculation """
def fibonacciI(n):
    if n <= 2:
        return 1
    else:
        newValue = 0 # f[n]
        previousValue = 1 # given from f[2]
        superPreviousValue = 1 # given from f[1]

        for i in range(3, n + 1):
            newValue = previousValue + superPreviousValue
            superPreviousValue = previousValue
            previousValue = newValue

    return newValue

if __name__ == "__main__":
    #import timeit

    print('* * * Fibonacci Printer * * *\n')

    n = int(input('Which Fibonacci number would you like to see?: '))
    if n > 0 and n < 46:
        start = time.time()
        print('\nFibonacci number ' + str(n) + ' is: ' + str(fibonacciR(n)) + '\n')
        end = time.time()
        totalTime = end - start

        #t = timeit.timeit("fibonacciR(" + str(n) + ")", setup="from __main__ import fibonacciR", number=1)

        print('This calculation required ' + '%.3f' % totalTime + ' seconds.\n')
        #print('Iterative Solution: ' + str(fibonacciI(int(n))))
    else:
        print('Error: entry must be from 1 to 45 inclusive.\n')
