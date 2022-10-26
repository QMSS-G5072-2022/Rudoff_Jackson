import pytest
from cipher import *
import pandas as pd 
from urllib.request import urlopen



def test_word():
    example = 'word'
    shift = 4
    expected = 'Asvh'
    actual = cipher(example, shift)
    assert actual == expected

def test_neg():
    test_text = "The New York Mets were once good at baseball and then they sucked"
    example_shift = -2
    expected = "Rfc Lcu Wmpi Kcrq ucpc mlac emmb Yr ZYqcZYjj Ylb rfcl rfcw qsaicb"
    actual = cipher(test_text, example_shift)
    assert actual == expected


def test_special():
    test_text = "UhOh!?!%"
    test_shift = 5
    expected = "ZmTm!?!%"
    actual = cipher(test_text, test_shift)
    assert expected == actual


def test_assert():
    with pytest.raises(Exception):
        test_word = "two"
        test_shift = "two"
        cipher(test_word,test_shift)

    