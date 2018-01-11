# Python Program for calculating the nth Fibonacci numbers
# f[n] = f[n - 1] + f[n - 2]

def fibonacciR(n):
    if n == 0:
        return 0
    elif n > 0 and n <= 2:
        return 1
    else:
        return fibonacciR(n - 1) + fibonacciR(n - 2)

def fibonacciI(n):
    if n == 0:
        return 0
    elif n > 0 and n <= 2:
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

    n = input('Enter the number of Fibonacci Numbers to calculate: ')

    print('Recursive Solution: ' + str(fibonacciR(int(n))))
    print('Iterative Solution: ' + str(fibonacciI(int(n))))
