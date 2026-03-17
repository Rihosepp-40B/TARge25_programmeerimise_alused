from solution import students_study, lottery

def test_students_18_to_24_any_true():
    assert students_study(18, True) == True
    assert students_study(21, True) == True
    assert students_study(24, True) == True
    assert students_study(18, False) == True
    assert students_study(21, False) == True
    assert students_study(24, False) == True
    assert students_study(18, "") == True
    assert students_study(21, "") == True
    assert students_study(24, "") == True


def test_students_5_to_17_true_true():
    assert students_study(5, True) == True
    assert students_study(11, True) == True
    assert students_study(17, True) == True


def test_students_5_to_17_false_or_text_false():
    assert students_study(5, False) == False
    assert students_study(11, False) == False
    assert students_study(17, False) == False
    assert students_study(5, "") == False
    assert students_study(11, "") == False
    assert students_study(17, "") == False


def test_students_0_to_4_any_false():
    assert students_study(0, False) == False
    assert students_study(2, False) == False
    assert students_study(4, False) == False
    assert students_study(0, True) == False
    assert students_study(2, True) == False
    assert students_study(4, True) == False
    assert students_study(0, "") == False
    assert students_study(2, "") == False
    assert students_study(4, "") == False


def test_students_time_string():
    assert students_study("", "") == False

    
def test_lottery_all_equal():
    assert lottery(5, 5, 5) == 10
    assert lottery(1, 1, 1) == 5
    assert lottery(10, 10, 10) == 5


def test_lottery_a_not_b_or_c():
    assert lottery(1, 2, 3) == 1
    assert lottery(1, 3, 3) == 1


def test_lottery_a_is_b_or_c():
    assert lottery(1, 2, 1) == 0
    assert lottery(1, 1, 3) == 0