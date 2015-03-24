def ack(m, n):

    """This module computes Ackermann function, which is a total computable 
    function that is not primitive recursive.
    """
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ack(m - 1, 1)
    if m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))

if __name__ == "__main__":
    assert ack(3, 4)
