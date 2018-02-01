def square(n):
    """
    (num) -> (num)
    Returns square root for some number
    """
    try:
        assert(type(n) is int)
        if n == 1:
            return 1
        s = square(n - 1) + 2*(n - 1) + 1
        return s
    except:
        return None
