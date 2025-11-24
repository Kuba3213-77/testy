import pytest
from main import read_int, prime_factors, print_factors
from io import StringIO


def test_read_int_valid(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('20\n'))
    assert read_int() == 20

def test_read_int_invalid(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('abc\n'))
    with pytest.raises(ValueError):
        read_int()

def test_read_int_negative(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('-7\n'))
    assert read_int() == -7

def test_read_int_zero(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('0\n'))
    assert read_int() == 0

def test_prime_factors_20():
    assert prime_factors(20) == [2,2,5]

def test_prime_factors_13():
    assert prime_factors(13) == [13]

def test_prime_factors_100():
    assert prime_factors(100) == [2,2,5,5]

def test_prime_factors_1():
    assert prime_factors(1) == []

def test_prime_factors_0():
    assert prime_factors(0) == []

def test_prime_factors_negative():
    assert prime_factors(-5) == []

def test_prime_factors_2():
    assert prime_factors(2) == [2]

def test_prime_factors_3():
    assert prime_factors(3) == [3]

def test_print_factors(capsys):
    print_factors([2,2,5])
    captured = capsys.readouterr()
    assert captured.out == "2\n2\n5\n"