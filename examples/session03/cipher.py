import random

alphabet = "abcdefghijklmnopqrstuvwxyz "

alphabet_list = [alphabet[i] for i in range(len(alphabet))]
#alphabet_list = list(alphabet)

print(alphabet_list)

message_text = "hello"

cipher_list =['v', 'y', 'h', 'l', 'a', 'n', 'i', 'g', 'e', 'd', 'k', 'c', 'w', ' ', 'f', 's', 'm', 'p', 'r', 't', 'o', 'u', 'z', 'b', 'j', 'x', 'q']

cipher_text = ""

for x in message_text:
    index = alphabet_list.index(x)
    cipher_char = cipher_list[index]
    cipher_text += cipher_char

print cipher_text
