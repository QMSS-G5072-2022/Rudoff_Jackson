import pytest
import pandas as pd
from cipher import *

@pytest.fixture
def words_csv():
    df = pd.read_csv('data/words.csv')
    return df

@pytest.mark.parametrize("example, shift, expected", [
    (0, 4, 'TCxlsr'),
    (1, 5, 'YJXYNSL'),
    (2, 7, 'kpmmpjBsA'), #intentionally false example
    (3, 8,'epG qA qB Aw lqnnqkCtB.')
])
def test_parametrize(words_csv, example, shift, expected):
    result = cipher(words_csv.loc[example]['Extract'], shift+1)
    assert result == expected