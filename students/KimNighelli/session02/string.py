'''
What I'm going to code: 
        Remove non alpha numeric characters
        Determine if something is a letter or number and return to two seperate lists
        something else

'''
def alpha_numeric(n):
        print n
        for element in n:
                if element.isalnum():
                        #print "%s is alnum!" %(element)
                        continue
                else:
                        #print "%s is not" % (element)
                        n = n.replace(element,"")
        print n

#alpha_numeric("!A!!")
#alpha_numeric("@@@...!!!>&#%@*!")
#alpha_numeric("kjfhhf!jfhg,...,lkifdjbf!")
#alpha_numeric("strrrrriiiiinnnngggg")

def letter_or_number(n):
        print n
        letters = []
        numbers = []

        for element in n:
                if element.isalpha():
                        letters.append(element)
                elif element.isdigit():
                        numbers.append(element)

        print letters
        print numbers

#letter_or_number("hello123        space         world")
#letter_or_number("!!$DDOWMC**1134")

def upper_lower_split(n):

    temp_list = []

    for i, element in enumerate(n.split(" ")):
        if i % 2 == 0:
            temp_list.append(element.upper())
        else:
            temp_list.append(element.lower())


    print " ".join(temp_list)



upper_lower_split("Hello my name is kim and I like to dance")

        
