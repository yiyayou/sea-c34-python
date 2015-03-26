"""
Can I write my own exception?"""
# define new class for my exception


class BadIdea(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

try:
    raise BadIdea(2*2)
except BadIdea as e:
    print 'My exception occurred, value:', e.value


"""Will the script still run after the exception has thrown?"""
for number in range(6):
    fraction = "undefined"
    try:                      # first action
        fraction = 6.0/number
    except ZeroDivisionError:  # runs if first action creates error
        print("you cannot divide by 0!")
    finally:
        print fraction  # runs no matter what
