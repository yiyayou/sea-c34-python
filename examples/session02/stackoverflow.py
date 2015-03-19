def runneth_over(x):
    while x < 10:
      runneth_over(x + 1)
    return x

runneth_over(1)
