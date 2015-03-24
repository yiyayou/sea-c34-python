def update_list_in_tuple(method='extend', new=['new', 'values']):
    """
    Check if tuple shows updated values of nested list.

    Args:
        method: the method to change list values.
        new: the new value(s) for the list.
    Returns:
        print out of test and result.

    """
    my_list = ['old', 'values']
    my_tuple = (0, 1, 2, my_list)
    msg = u"my_list is {my_list}, and my_tuple is {my_tuple}.\n" \
        .format(my_list=my_list, my_tuple=my_tuple)
    if method == 'append':
        my_list.append(new)
    elif method == 'extend':
        my_list.extend(new)
    elif method == 'replace':
        my_list = new
    else:
        print(u"Please use append, extend, or replace.")
        return
    msg += u"my_list has been updated to {my_list}.\n".format(my_list=my_list)
    msg += u"my_list is now {my_list}, and my_tuple is {my_tuple}.\n" \
        .format(my_list=my_list, my_tuple=my_tuple)
    print(msg)
    try:
        assert(my_list == my_tuple[3])
        print(u"The new values were updated in the tuple.")
    except:
        print(u"The new values did not update in the tuple.")


# update_list_in_tuple()
# result: value reassignment is not updated in tuple; modification is.
