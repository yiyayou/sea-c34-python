'''
What I'm going to code:

        reduce the some string from each side - good for now!
        count the number of evens/odds in a list
        list the numbers between -1

'''

'''
def reduce_length(n):
        max_iteration = len(n)/2

        print n
        for i in range(1,max_iteration+1):
                print n[i:-i]

reduce_length("tententen")
reduce_length("lkjfhfdjkghfbgfvjhgbvxjkdfhjgdfdkvicvyudfbjdbcvyadfk")
'''
'''
def count_even_odd(n):
        count_even = 0
        count_odd = 0

        print "Searching over list %s" % (n)

        for element in n:
                if element % 2 == 0:
                        print "%s is an even number. Adding to even count." % (element)
                        count_even = count_even + 1
                else:
                        print "%s is an odd number. Adding to odd count." %(element)
                        count_odd = count_odd + 1

        print "The number of even variables in the list is %s" % (count_even)
        print "The number of odd variables in the list is %s" % (count_odd)

count_even_odd([6,5,2,5,7,8,9,4,3,2,2])
count_even_odd([0,0,0,0,0])
count_even_odd([-1,0,1,2])
'''

def numbers_between_neg1(orig_list):
        between_list = []
        flag = False

        for i in orig_list:
                print i
                print flag
                if flag == True:
                        between_list.append(i)
                elif i == -1 and flag == False:
                        flag = True
                elif i == -1 and flag == True:
                        flag = False

        print between_list

numbers_between_neg1([6,4,-1,3,6,7,2,-2,1,56,-1,45,3])
