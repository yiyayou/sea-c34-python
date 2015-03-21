import string
import codecs  # Use for validation testing

user = str(raw_input("Message to encrypt: "))
chars = string.maketrans(
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")


def rot13(user):
    message = string.translate(user, chars)
    print(message)


if __name__ == "__main__":
    assert(rot13(user) == codecs.encode(user, "rot_13"))
