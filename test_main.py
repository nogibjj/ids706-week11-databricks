from main import main
def test_max():
    """Function calling listMax"""

    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [1, 2, 3, 4]
    assert main(list1) == 6
    assert main(list2) == 4
