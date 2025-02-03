def lists():
    first_list = [1, 2, 3, 4, 5]

    print(first_list)  # [1, 2, 3, 4, 5]
    print(first_list[2])  # 3
    print(first_list[-1])  # 5
    print(first_list[1:3]) # [2, 3]
    print(first_list[2:])  # [3, 4, 5]
    print(first_list[:3])  # [1, 2, 3]
    print(first_list[::2])  # [1, 3, 5]
    print(first_list[::-1])  # [5, 4, 3, 2, 1]
    print(first_list[1:4:2])  # [2, 4]
    print(first_list + [6, 7, 8])  # [1, 2, 3, 4, 5, 6, 7, 8]

    second_list = list()
    print(second_list)  # []
    second_list.append(10)  # [10]
    print(second_list)  # [10]
    second_list.extend([11, 12, 13])  # [10, 11, 12, 13]
    print(second_list) # [10, 11, 12, 13]
    second_list.insert(1, 20)  # [10, 20, 11, 12, 13]
    print(second_list)
    second_list.remove(11)  # [10, 20, 12, 13]
    print(second_list)


def dictionaries():
    first_dictionary = {
        "key1": 1,
        "key2": 2,
        "key3": 3
    }
    print(first_dictionary)  # {'key1': 1, 'key2': 2, 'key3': 3}
    print(first_dictionary["key2"]) # 2
    print(first_dictionary.get("key4"))  # None
    print(first_dictionary.get("key4", 4))  # 4
    print(first_dictionary.get("key3", 4))  # 3
    print(first_dictionary.keys())  # ['key1', 'key2', 'key3']
    print(first_dictionary.values())  # [1, 2, 3]
    print(first_dictionary.items())  # [('key1', 1), ('key2', 2), ('key3', 3)]

    for key in first_dictionary.keys():
        print(key, first_dictionary[key])

    for key, value in first_dictionary.items():
        print(key, value)

    second_dictionary = dict()
    print(second_dictionary)  # {}
    second_dictionary["key1"] = 10  # {'key1': 10}
    print(second_dictionary)
    second_dictionary.update({"key2": 20, "key3": 30})  # {'key1': 10, 'key2': 20, 'key3': 30}
    print(second_dictionary)
    value = second_dictionary.pop("key2")  # {'key1': 10, 'key3': 30}
    print(value)
    print(second_dictionary)


if __name__ == "__main__":
    lists()
    dictionaries()
