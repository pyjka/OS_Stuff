""" Given a positive integer N, print all the integers from 1 to N.
But for multiples of 3 print “Fizz” instead of the number and for the multiples of 5 print “Buzz”. 
Also for number which are multiple of 3 and 5, prints “FizzBuzz”.
"""

def fizzBuzz(A):
    arr = []
    for i in range(1,A+1):
        if i % 3 == 0 and i % 5 == 0:
            arr.append('FizzBuzz')
        elif i % 5 == 0:
            arr.append('Buzz')
        elif i % 3 == 0:
            arr.append('Fizz')
        else:
            arr.append(i)
    return arr