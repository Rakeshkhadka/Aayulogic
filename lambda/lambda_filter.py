def take_input():
    try:
        data = input("Enter a list of integers separated by comma: ")
        data = list(map(int, data.split(',')))
        return data
    except ValueError:
        print("Error: Invalid input")
        return []


def main():
    data =  take_input()
    new_list = list(filter(lambda x : x%2==0, data))
    print(f"Even number from the given list is {new_list}" )

if __name__ == "__main__":
    main()