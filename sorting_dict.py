my_dict = {"apple": 3, "banana": 2, "orange": 5, "pear": 1}

j = list(my_dict.items())
k = []
for i in range(len(j)):
    for m in range(i+1, len(j)-1):
        if j[i][1] < j[m][1]:
            j[i], j[m] = j[m], j[i]

print(j)
new_dict = {}
for i in range(len(j)):
    new_dict.update( { j[i][0] : j[i][1]} ) 
print(new_dict)