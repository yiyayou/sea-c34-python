def squirrel_party(cigars, weekend):
    """
    Return whether squirrel party is successful.
    Args:
        cigars (int): number of cigars smoked
        weekend (book): whether is weekend

    Return:
        return whether between 40 and 60 cigars inclusive
        if on a weekday, and otherwise on weekends, at least 40

    """
    if (not weekend) and ((cigars >= 40) and (cigars <= 60))
        return True
    else:
        return False


if __name__ == "main":
    if (squirrel_party(40, False)):
        print ("Successful weekday party")
    else
        print ("It Bombed")
