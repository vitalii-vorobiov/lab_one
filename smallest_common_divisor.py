def scd(n, m):
    """
    (int), (int) -> int
    Returns the smallest common divisor of two numbers
    """
    try:
        assert(type(n) is int)
        assert(type(m) is int)
        if n < m:
            return scd(n, m - n)
        elif n > m:
            return scd(n - m, m)
        elif n == m:
            return n
    except:
        return None
