import pytest
from unittest.mock import patch, MagicMock
from bank import Bank

@pytest.fixture(scope='function')
def bank_obj():
    return Bank(100)

def test_credit_ok(bank_obj):
    result2 = 200
    amt = 100
    assert bank_obj.credit(amt) == result2

def test_credit_invalid(bank_obj):
    with pytest.raises(Exception, match="Amount should be -ve"):
        bank_obj.credit(-1)

def test_debit_ok(bank_obj):
    result2 = 90
    amt = 10
    assert bank_obj.debit(amt) == result2

def test_debit_invalid(bank_obj):
    amt = 1000
    with pytest.raises(Exception, match="Cannot withdraw"):
        bank_obj.debit(amt)

@patch.object(Bank, 'credit', return_value=200)
@patch.object(Bank, 'debit', return_value=100)
def test_calculation(mock_debit, mock_credit, bank_obj):
    # Call the calculation method and assert the result
    assert bank_obj.calculation() == 100