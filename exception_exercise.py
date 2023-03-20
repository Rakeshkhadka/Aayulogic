def take_input():
    input_text = input("Enter a text:")
    return input_text

def check_type(my_input):
    try:
        value = int(my_input)
        print(f"{my_input} is integer")
    except ValueError:
        print('-----',ValueError.__dict__)
        try:
            value = float(my_input)
            print(f"{my_input} is float")
        except ValueError as te:
            print('-----',te)
            print(f"{my_input} is string")

x = take_input()
check_type(x)