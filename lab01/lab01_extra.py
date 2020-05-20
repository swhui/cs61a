"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    s = 1
    a = n
    while n > (a-k):
        s = s*n
        n = n-1
    return s

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    a = 0
    while n > 0:
        n1 = n % 10
        n2 = n // 10 % 10
        if n1 == 8 and n2 == 8:
            a = a+1
        else:
            a = a+0
        n = n // 10
    if a > 0:
        return True
    else:
        return False
