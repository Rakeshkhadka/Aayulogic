# try:
#     print(x)
# except:
#     print(" x is not initialized")


# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("envountered 0 on divisor")
# except:
#     print("invalid")



# try:
#     with open("data.csv") as file:
#         file.read()
# except FileNotFoundError as fnf:
#     print(fnf)
#     print("File Not found")


# def find_nth(x, n):
#     try:
#         value = (x[n])
#     except IndexError as IE:
#         print(IE)
#     else:
#         print(value)


# y = [2, 3, 4, 5]
# find_nth(y, 6)

def divise(x, y):
    try:
        value =  x/y
    except ZeroDivisionError as Ze:
        print(Ze)
        print("change the value of y")
    except:
        print("Invalid")
    else:
        print(f"{x} divided by {y} is {value}")
    finally:
        print("Code ran successfully")

def input1():
    a = int(input("Enter A: "))
    b = int(input("Input B: "))
    divise(a, b)

input1()