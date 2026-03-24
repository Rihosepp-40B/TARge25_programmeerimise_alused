"""Dictionary exercises."""


def get_hobbies(hobbies_dict: dict, name: str) -> list:
    """
    Return the hobbies of a given person.

    hobbies = {
    "Tom": ["running", "reading"],
    "John": ["movies", "music", "swimming"]
    }

    get_hobbies(hobbies, "Tom")  => ["running", "reading"]
    get_hobbies(hobbies, "Timmy")  => "name not in dictionary"

    :param hobbies_dict: dictionary with peoples' hobbies.
    :param name: name of person whose hobbies are to be returned.

    :return: List of hobbies of the person with given name or "name not in dictionary".
    """
    if name in hobbies_dict:
        result_list = hobbies_dict[name]
    else:
        result_list = "name not in dictionary"
    return result_list


def find_tallest(height_dict: dict) -> None:
    """
    Return the name of the tallest peron in given dictionary.

    find_tallest({"Tom": 186, "Mari": 175, "Jhon": 190}) => "Jhon"

    :param height_dict: dictionary with peoples' names and heights
    :return name of tallest person in given dict.
    """
    max_height = max(height_dict.values())
    for name in height_dict:
        if height_dict[name] == max_height:
            return name


def remove_sixes(six_dict: dict) -> dict:
    """
    Return a dictionary where all keys which's values are dividable by six are removed.

    remove_sixes({"a": 4, "b": 8, "c": 6, "d": 18}) => {"a": 4, "b": 8}

    :param six_dict: dictionary to be modified.
    :return: dict without values that are dividable by six.
    """
    keys_to_delete = []
    for k in six_dict:
        if six_dict[k] % 6 == 0:
            keys_to_delete.append(k)
    for k in keys_to_delete:
        del six_dict[k]
    return six_dict


def exchange_keys_and_values(exchange_dict: dict) -> dict:
    """
    Return a dict where keys and values have been exchanged.

    exchange_keys_and_values({"a": "b", "c": "d"}) => {"b": "a", "d": "c"}

    :param exchange_dict: dictionary to be modified.
    :return dictionary where values and keys have been exchanged.
    """
    edited_dict = {}
    for k in exchange_dict:
        edited_dict[exchange_dict[k]] = k
    return edited_dict


def count_symbol_appearances(stringy: str) -> dict:
    """
    Return dict where key is the symbol and the value is the count this symbol is present in the string.

    count_symbol_appearances("hello hi") => {'h': 2, 'e': 1, 'l': 2, 'o': 1, ' ': 1, 'i': 1}

    :param stringy: string to be processed.
    :return: dictionary with symbol counts.
    """
    length = len(stringy)
    done = []
    return_dictionary = {}
    for i in range(length):
        if done.count(stringy[i]) == 0:
            key = stringy[i]
            value = stringy.count(key)
            return_dictionary[key] = value
    return return_dictionary


def organise_by_first_symbol(strings: list) -> dict:
    """
    Return dict where key the is a symbol and the value is a list of words starting with this symbol.

    organise_by_first_symbol(["hello", "word", "world", "welcome", "yes"]) =>
        {'h': ['hello'], 'w': ['word', 'world', 'welcome'], 'y': ['yes']}

    :param strings: list of strings.
    :return: dict with starting symbol and corresponding words in order of appearance.
    """
    # lühem versioon:
    """
    new_dictionary = {}
    for i in strings:
        key = i[0]
        new_dictionary.setdefault(key, []).append(i)
    return new_dictionary
    """

    new_dictionary = {}
    for i in range(len(strings)):
        key = strings[i][0]
        value = strings[i]
        new_dictionary.setdefault(key, []).append(value)
    return new_dictionary

if __name__ == "__main__":
    """hobbies = {
        "Tom": ["running", "reading"],
        "John": ["movies", "music", "swimming"]
    }
    print(get_hobbies(hobbies, "Tom"))
    print(get_hobbies(hobbies, "Timmy"))

    heights = {"Tom": 186, "Mari": 175, "Jhon": 190}
    print(find_tallest(heights))

    numbers_dict = {"a": 4, "b": 8, "c": 6, "d": 18}
    print(remove_sixes(numbers_dict))

    dict_to_exchange = {"a": "b", "c": "d"}
    print(exchange_keys_and_values(dict_to_exchange))
    word = "hello hi"
    print(count_symbol_appearances(word))

    word_list = ["hello", "word", "world", "welcome", "yes"]
    print(organise_by_first_symbol(word_list))"""