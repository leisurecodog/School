"""This script tests the Fibonacci class and fibonacci_gen"""

from fibonacci import Fibonacci
from fibonacci import fibonacci_gen
 
if __name__ == '__main__':
    # test Fibonacci class
    f = Fibonacci(10)
    
    print(f)
    # => The first 10 Fibonacci numbers are [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    
    print(f.get_nums())
    # => [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] 
    
    for item in Fibonacci(8):
        print(item,end=' ')
        # => 0 1 1 2 3 5 8 13 
    print()
    # test fibonacci generator
    for i in fibonacci_gen(12):
        print(i,end=' ')
    print()
        # => 0 1 1 2 3 5 8 13 21 34 55 89
        
    f_gen = fibonacci_gen()
    for i in range(30):
        print(next(f_gen),end=' ')
    print()
        # => 0 1 1 2 3 5 8 13 21 34 55 89 144 … (a total of 30 numbers)
