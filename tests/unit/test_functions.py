from chess_functions import check_input
import pytest


def test_check_input():
    assert check_input("a1 a2") == True
    assert check_input("a1 a2 a3") == False
    assert check_input("-1") == False
    assert check_input("A1 B3") == False
    assert check_input("J1 A3") == False
