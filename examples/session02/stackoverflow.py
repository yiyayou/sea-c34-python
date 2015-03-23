def runneth_over(a):
    print a
    a += 1
    runneth_over(a)

runneth_over(0)
