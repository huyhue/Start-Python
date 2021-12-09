import string
import random

# LETTERS = string.ascii_letters
# print(LETTERS)
print(string.__file__)
# NUMBERS = string.digits
# PUNCTUATION = string.punctuation

# def get_password_length():
#     password_length = input("How long do you want your password: ")
#     return int(password_length)

# def password_generator(lenght=8):
#     printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'
#     printable = list(printable)
#     random.shuffle(printable)

#     random_password = random.choices(printable, k=lenght)
#     random_password = ''.join(random_password)
#     return random_password

# def main():
#     password_length = get_password_length()
#     password = password_generator(password_length)
#     print(password)

# if __name__ == "__main__":
#     main()