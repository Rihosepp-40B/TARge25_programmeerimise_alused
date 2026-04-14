"""Test Hobbies functions"""


from main import *


MariKukk = Person("Mari", "Kukk", ["dancing", "biking", "programming"])
JeffBezos = Person("Jeff", "Bezos", ["money", "hair", "late_capitalism", "space", "unions"])
ElonMusk = Person("Elon", "Musk", ["late_capitalism", "space", "cars"])


def init_tests():
    return [MariKukk, JeffBezos, ElonMusk]


def test_sort_by_most_hobbies():
    people = init_tests()
    assert sort_by_most_hobbies(people) == [JeffBezos, ElonMusk, MariKukk]


def test_by_least_hobbies():
    people = init_tests()
    assert sort_by_least_hobbies(people) == [ElonMusk, MariKukk, JeffBezos]


def test_filter_by_hobby():
    people = init_tests()
    assert filter_by_hobby(people, "space") == [ElonMusk, JeffBezos]


def test_sort_people_and_hobbies():
    people = init_tests()
    assert sort_people_and_hobbies(people) == [ElonMusk, JeffBezos, MariKukk]
    assert MariKukk.hobbies == ['biking', 'dancing', 'programming']