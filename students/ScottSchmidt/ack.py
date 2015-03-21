def ack(m, n):
    if m < 0 or n < 0:
        return "Invalid argument, must be absolute integers."
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    else:
        return ack(m-1, ack(m, n-1))


if __name__ == "__main__":
    if ack(2, 2) == 7:
        print "Test OK"
    if ack(3, 4) == 125:
        print "Test OK"
