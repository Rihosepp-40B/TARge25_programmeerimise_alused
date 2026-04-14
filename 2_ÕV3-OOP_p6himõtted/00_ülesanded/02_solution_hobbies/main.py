"""Hobbies but OOP."""


from person import Person


def filter_by_hobby(people_list: list, hobby: str) -> list:
    """
    Return list of people that have the given hobby in their list of hobbies.

    :param people_list: input list of people.
    :param hobby: hobby to filter by.
    :return: filtered list of people.
    """
    names_sorted = sort_people_and_hobbies(people_list)
    return [p for p in names_sorted if hobby in p.hobbies]  # järjendisse p kui p järjendist omab hobi


def sort_by_most_hobbies(people_list: list) -> list:
    """
    Return a list of people sorted by amount of hobbies in descending order.

    Highest amount of hobbies first.
    If they have the same amount of hobbies, then by full name alphabetically.

    :param people_list: list of people to sort.
    :return: sorted list of people.
    """
    names_sorted = sort_people_and_hobbies(people_list)
    return sorted(names_sorted, key=lambda p: len(p.hobbies), reverse=True)


def sort_by_least_hobbies(people_list: list) -> list:
    """
    Return a list of people sorted by amount of hobbies in ascending order.

    Least amount of hobbies first.
    If they have the same amount of hobbies, then by full name alphabetically.

    :param people_list: list of people to sort.
    :return: sorted list of people.
    """
    names_sorted = sort_people_and_hobbies(people_list)
    return sorted(names_sorted, key=lambda p: len(p.hobbies))


def sort_people_and_hobbies(people_list: list) -> list:
    """
    Return the list of people but sorted alphabetically by their full name.

    Also sort their list of hobbies.

    :param people_list: list of people to sort.
    :return: sorted list of people.
    """
    sorted_list = sorted(people_list, key=lambda p: p.full_name)
    for p in sorted_list:
        p.hobbies.sort()
    return sorted_list


if __name__ == '__main__':
    person1 = Person("Mari", "Kukk", ["dancing", "biking", "programming"])
    person2 = Person("Jeff", "Bezos", ["money", "hair", "late_capitalism", "space", "unions"])
    person3 = Person("Elon", "Musk", ["late_capitalism", "space", "cars"])
    people = [person1, person2, person3]
    print(sort_by_most_hobbies(people))  # -> [JeffBezos, ElonMusk, MariKukk]
    print(sort_by_least_hobbies(people))   # -> [ElonMusk, MariKukk, JeffBezos]
    print(filter_by_hobby(people, "space"))  # -> [ElonMusk, JeffBezos]
    print(sort_people_and_hobbies(people))  # -> [ElonMusk, JeffBezos, MariKukk]
    print(person1.hobbies)  # -> ['biking', 'dancing', 'programming']
