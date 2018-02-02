def recursion(n, m):
    """
    This function return sum of 1^m + 2^m + ... + n^m

    (int, int) -> (int)
    >>> recursion(5,3)
    225
    >>> recursion(0.4,0.1)
    'Input whole positive numbers!'
    >>> recursion('abc','c')
    'Input whole positive numbers!'

    """
    try:
        return 'Input whole positive numbers!' if n <= 0 or m <= 0 else n**m \
        if n == 1 else n**m + recursion(n-1, m)
    except TypeError:
        return 'Input whole positive numbers!'

print(recursion(5,2))
