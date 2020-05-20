def in_nested(v, L):
    """
    >>> in_nested(5, [1, 2, [[3], 4]])
    False
    >>> in_nested(9, [[[1], [6, 4, [5, [9]]], 7], 7, 7])
    True
    >>> in_nested(1, 1)
    True
    """
    if type(L) != list:
        return L == v
    else:
        return True in [in_nested(v, element) for element in L]


class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        self.first = first
        self.rest = rest
        def __str__(self):
            string = '<'
            while self.rest is not Link.empty:
                string += str(self.first) + ', '
                self = self.rest
                return string + str(self.first) + '>'


def link_to_dict(L):
    """
    >>> L = Link(1, Link(2, Link(3, Link(4, Link(1, Link(5))))))
    >>> print(L)
    <1, 2, 3, 4, 1, 5>
    >>> link_to_dict(L)
    {1: [2, 5], 3: [4]}
    >>> print(L)
    <1, 3, 1>
    """
    D = {}
    while L is not Link.empty:
        key, value = L.first, L.rest.first
        if key not in D:
            D[key] = value
        else:
            D[key].append(value)
    return D


def plus(n):
    """Return the largest sum that results from inserting +'s into n.
    >>> plus(123456) # 12 + 34 + 56 = 102
    102
    >>> plus(1604) # 1 + 60 + 4 = 65
    65
    >>> plus(160450) # 1 + 60 + 4 + 50 = 115
    115
    """
    if n:
        return max(plus(n//100)+n%100, plus(n//10) + n %10)
    return 0

def plusses(n, cap):
    """Return the number of plus expressions for n with values below cap.
    >>> plusses(123, 16) # 1+2+3=6 and 12+3=15, but 1+23=24 isn't below cap.
    2
    >>> plusses(2018, 38) # 2+0+1+8, 20+1+8, 2+0+18, and 2+01+8, but not 20+18.
    4
    >>> plusses(1, 2)
    1
    """
    if n < 10 and n < cap:
        return 1
    elif cap <= 0:
        return 0
    else:
        return plusses(n // 10, cap - n % 10) + plusses(n // 100, cap - n % 100 )
