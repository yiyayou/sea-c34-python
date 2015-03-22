
def cigar_party(cigars, weekend):
    """
    Return whether squirrl party is successful.

    Args:
        cigars (int): number of cigars smoked
        weekend (boolean): whether or not it is a weekend
    Return: 
        whether there were between 40 and 60 cigars inclusive if on a weekday,

    """
    if (not weekend) and ((cigars >= 40) and (cigars <= 60)):
        return True
    elif ()

    else:
        return False

if __name__ == '__main__':
    print(cigar_party(30, False))
    print(cigar_party(50, False))
    print(cigar_party(70, True))