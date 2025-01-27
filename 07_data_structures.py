def lists():
    first_list = [1, 2, 3, 4, 5]

    print(first_list)
    print(first_list[2])
    print(first_list[-1])
    print(first_list[1:3])
    print(first_list[2:])
    print(first_list[:3])
    print(first_list[::2])
    print(first_list[::-1])
    print(first_list[1:4:2])
    print(first_list + [6, 7, 8])

    second_list = list()
    print(second_list)
    second_list.append(10)
    print(second_list)
    second_list.extend([11, 12, 13])
    print(second_list)
    second_list.insert(1, 20)
    print(second_list)
    second_list.remove(11)
    print(second_list)


def dictionaries():
    first_dictionary = {"key1": 1, "key2": 2, "key3": 3}
    print(first_dictionary)
    print(first_dictionary["key2"])
    print(first_dictionary.get("key4"))
    print(first_dictionary.get("key4", 4))
    print(first_dictionary.keys())
    print(first_dictionary.values())
    print(first_dictionary.items())

    second_dictionary = dict()
    print(second_dictionary)
    second_dictionary["key1"] = 10
    print(second_dictionary)
    second_dictionary.update({"key2": 20, "key3": 30})
    print(second_dictionary)
    value = second_dictionary.pop("key2")
    print(value)
    print(second_dictionary)


if __name__ == "__main__":
    lists()
    dictionaries()
