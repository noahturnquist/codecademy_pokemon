lst_values = []
lst_keys = []
dicts = {"a": 1, "b": 2}

def loopit():
    for key, value in dicts.items():
        lst_values.append(value)
        lst_keys.append(key)

loopit()

print (lst_values[1])
print (lst_keys)