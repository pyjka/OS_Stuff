import operator
import re

def calc(expr):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.div
    }

    arr = []
    new_arr = []

    for i,j in enumerate(expr):
        if j != ' ':
            arr.append(j)

    for i in expr:
        if set(i).issubset(set('1234567890')):
            new_arr.append(int(i))
        if i in ops and expr:
            a = new_arr.pop()
            b = new_arr.pop()
            op = ops[i]
            x = new_arr.append(op(b,a))
    #final = ''.join(map(str,new_arr))
    print new_arr[0] # or return and print func.

if __name__ == '__main__':
    print ('RPN expression has to be a string')
    calc(raw_input('Enter RPN expression :'))

