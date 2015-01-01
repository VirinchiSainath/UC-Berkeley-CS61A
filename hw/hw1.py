# CS 61A Fall 2014
# Name:
# Login:

# http://www-inst.eecs.berkeley.edu/~cs61a/fa14/hw/released/hw1.html

from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    # BEGIN SOLUTION

    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

    # END SOLUTION

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c. Use only one epression

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    # BEGIN SOLUTION

    return max(a, b, c) * max(a, b, c) + min(max(a, b), max(b, c), max(a, c)) * min(max(a, b), max(b, c), max(a, c))

    # END SOLUTION

def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result

def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

def with_if_function():
    return if_function(c(), t(), f())

def c():
    # BEGIN SOLUTION

    return 1 > 0

    # END SOLUTION

def t():
    # BEGIN SOLUTION

    return 1

    # END SOLUTION

def f():
    # BEGIN SOLUTION

    return 0

    # END SOLUTION

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """

    Pick a positive integer n as the start.
If n is even, divide it by 2.
If n is odd, multiply it by 3 and add 1.
Continue this process until n is 1.


    # BEGIN SOLUTION

     while n != 1:
        if n % 2 == 0: #even
            n = n / 2
            print (n)
        else: #odd
            n = n*3+1
            print (n)

    # END SOLUTION

challenge_question_program = """
"*** YOUR CODE HERE ***"
"""


