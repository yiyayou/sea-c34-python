""" When squirrels get together for a party, they like to have cigars.
A squirrel party is successful when the number of cigars is between 40 and 60,
inclusive. Unless it is the weekend, in which case there is no upper bound on
the number of cigars. Return True if the party with the given values is
successful, or False otherwise."""


def cigar_party(cigars, is_weekend):
    """ Return whether squirrel party is successful.

    Args:
        cigars (int): number of cigars smoked
        weekend (boolean): whether or not it is a weekend

    Return:
        whether there were between 40 and 60 cigars inclusive
        if on a weekday, and otherwise on weekends you cannot have
        enough cigars """
    if is_weekend is True:
        if cigars >= 40:
            return True
    elif cigars >= 40 and cigars <= 60:
        return True

    return False

if __name__ == "main":
    if cigar_party(40, False):
        print("Successful weekday party!")
    else:
        print("It Bombed!")
