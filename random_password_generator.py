import random
import string

def random_password_generator(length):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    number = string.digits
    special = string.punctuation

    needed_list = [upper, lower, number, special]
    char = "".join(needed_list)
    password = [random.choice(i) for i in needed_list] + [random.choice(char) for _ in range(length-4)]
    random.shuffle(password)
    return f"".join(password)





print(random_password_generator(8))
print(random_password_generator(8))
print(random_password_generator(8))
print(random_password_generator(9))
print(random_password_generator(9))
print(random_password_generator(9))
