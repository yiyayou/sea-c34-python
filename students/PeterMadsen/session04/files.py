import io 

def queston_one():
    """How would you draw a geometric feature in a  text file?"""
    try: 
        f = io.open('test.txt', 'w')
    except IOError:
        print ("That file doesn't exist at that location")

    space = 1
    for i in range(20):
        f.write(u'x')
        for j in range(space):
            f.write(u' ')
            j += 1
        f.write(u'x\n')
        space += 1
        if space > 20:
            break

def question_two():
    pass

if __name__ == '__main__':
    print("Running Question One: ")
    queston_one()
    print("Running Question Two: ")
    question_two()