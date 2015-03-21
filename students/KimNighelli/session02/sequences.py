'''
What I'm going to code:

        reduce the some string from each side - good for now!
        count the number of evens/odds in a list
        list the numbers between -1

'''

'''
'''
def reduce_length(n):
    max_iteration = len(n)/2

    print n
    for i in range(1, max_iteration+1):
        print n[i:-i]

def every_other(n):

    print n
    print n[::2]

every_other("abcdefghijklmnopqrstuvwxyz")

def count_even_odd(n):
    count_even = 0
    count_odd = 0

    print "Searching over list %s" % (n)

    for element in n:
        if element % 2 == 0:
            print "%s is an even number. Adding to even count." % (element)
            count_even += 1
        else:
            print "%s is an odd number. Adding to odd count." % (element)
            count_odd += 1

    print "The number of even variables in the list is %d" % (count_even)
    print "The number of odd variables in the list is %d" % (count_odd)


#reduce_length("adda")
#reduce_length("tententen")
#reduce_length("lkjfhfdjkghfbgfvjhgbvxjkdfhjgdfdkvicvyudfbjdbcvyadfk")

#count_even_odd([6,5,2,5,7,8,9,4,3,2,2])
#count_even_odd([0,0,0,0,0])
#count_even_odd([-1,0,1,2])


def pallindrome(x):
        if x == x[::-1]:
                print "%s is a pallindrome!" % (x)
        else:
               print "%s is not a pallindrome" % (x)

#pallindrome("abcba")
#pallindrome("definitelyNot")
