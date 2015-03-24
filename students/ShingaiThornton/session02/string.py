
#Q1: Can the .format() method be used on the same line as named place holders?

def placeHolding():
    """
    Args: 
    Returns:

    """
    print "Hi, {}, how's your {} ?  And your %s ?".format("Bob", "wife") %('kids')

#Q2: Can the raw_input function accept a list as input?

def listinput():
    """ Ask the user to enter a list

    Args:
    Returns:
    """
    list = raw_input('Please enter a list')
    print list


#Q3: Will calling .upper() .lower() and .title() on numeric types produce an error?

def numberOperations():
    """ Call the upper function on the number 42
    Args:

    Returns:
    """
    x = 42
    x.upper
    x.lower()
    x.title()