'''
What I'm going to code:

        Print right triangle
        Print equilateral triangle
        is the word a pallendrome?
'''

def right_triangle(n):
        for i in range(1, n+1):
                print "*" * i


#right_triangle(7)
#right_triangle(45)

def equi_triangle():
        height = int(raw_input("What height would you like the equilateral triangle? "))
        character = raw_input("What character should we use to make the triangle? ")
        #height = 4
        #character = "*"

        space_char = " "
        for i in range(height):
            print (space_char * (height - i - 1)) + ((character + space_char) * (i+1))
        

equi_triangle()


def numbers_between_neg1(orig_list):
    between_list = []
    flag = False

    for i in orig_list:
        print i
        print flag
        if i == -1 and flag == False:
            flag = True
        elif i == -1 and flag == True:
            flag = False
        elif flag == True:
            between_list.append(i)

    print between_list

numbers_between_neg1([6,4,-1,3,6,7,2,-2,1,56,-1,45,3])
