def fibonacci(x):
    """



    """
    a = 0
    y = 0
    my_list = [];


    while (y < x):
        print y
        #x = fibo[x] + y
        #print(fibo[y-1])
        #a = my_list[y-1]
        print a
        #my_list.append(my_list[y-1] + my_list[y-2])
        if a == 0:
            my_list.append(a)
            y = 1
            a = y
            print "this is zero"

        if a == 1:
            my_list.append(a)
            y = 2
            a = y
            print "this is one"
        #print my_list[y-1]
        #a = my_list[y-1]
        my_list.append(my_list[y-1] + my_list[y-2])
        print(my_list)

        y = y+a
        a = y


if __name__ == "__main__":
    fibonacci(10)
