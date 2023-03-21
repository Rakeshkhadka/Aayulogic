def take_input():
    try:
        x = input("Enter a list of integers separated by comma ")
        x = list(map(int, x.split(', ')))
        return x
    except ValueError:
        print("Invalid input")
        return []
def main():
    y = take_input()
    new_list= list(map(lambda x : x*x, y))
    print(new_list)

if __name__ == "__main__":
    main()