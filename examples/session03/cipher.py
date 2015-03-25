import random

alphabet = "abcdefghijklmnopqrstuvwxyz "
cipher = "vyhlanigedkcw fsmprtouzbjxq"

alphabet_list = [alphabet[i] for i in range(len(alphabet))]
# alphabet_list = list(alphabet)

message_text = "we should have an enchilada party"
decode_text = raw_input("Enter your code: ")

cipher_list = [cipher[i] for i in range(len(cipher))]

cipher_text = ""

for x in message_text:
    index = alphabet_list.index(x)
    cipher_char = cipher_list[index]
    cipher_text += cipher_char

print cipher_text

alphabet_text = ""

for x in decode_text:
    index = cipher_list.index(x)
    decode_char = alphabet_list[index]
    alphabet_text += decode_char

print alphabet_text
