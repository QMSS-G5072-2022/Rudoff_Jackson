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
    result = cipher(words_csv.loc[example]['Extract'], shift)
    assert result == expected

@pytest.mark.parametrize("example, shift", [
    ('It', 1),
    ('was', 2),
    ('the', 3),
    ('best', 4),
    ('of', 5),
    ('times', 6),
    ('it', 7),
    ('was', 8),
    ('the', 9),
    ('worst', 10),
    ('of', 11),
    ('times', 12)
])

def test_integration(example, shift):
    encrypt = cipher(example, shift, encrypt=True)
    decrypt = cipher(encrypt, shift, encrypt=False)
    assert decrypt == example