from functools import reduce
def take_input():
    try:
        data = input("Enter a list of integers separated by comma: ")
        data = list(map(int, data.split(',')))
        return data
    except ValueError:
        print("Error: Invalid input")
        return []

def main():
    a = take_input()
    z= reduce(lambda x,y : x+y, a)
    print(z)
if __name__ == "__main__":
    main()