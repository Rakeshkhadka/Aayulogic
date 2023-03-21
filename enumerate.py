my_list = [5, 7, 2, 9]
for index, item in enumerate(my_list, start=1):
    print(index, item)

my_dict = {"a": 1, "b": 2, "c": 3}
for index, item in enumerate(my_dict):
    print(index, item, my_dict[item])