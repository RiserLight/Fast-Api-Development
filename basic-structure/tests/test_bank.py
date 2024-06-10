import pytest
from unittest.mock import patch,AsyncMock
from bank import Bank

@pytest.fixture(scope='function')
def bank_obj():
  return Bank(100)

def test_credit_ok(bank_obj):
  result2=200
  amt=100
  assert bank_obj.credit(amt)==result2

def test_credit_invalid(bank_obj):
  with pytest.raises(Exception,match="Amount should be -ve"):
    bank_obj.credit(-1)



async def test_debit_ok(bank_obj):
  result2=90
  amt=10
  assert  bank_obj.debit(amt)==result2


async def test_debit_invalid(bank_obj):
  amt=1000
  with pytest.raises(Exception,match="Cannot withdraw"):
     bank_obj.debit(amt)


@patch('bank.credit')
@patch('bank.debit')
async def test_calculation(mock_debit,mock_credit,bank_obj):
  print(dir(mock_credit))
  mock_credit.return_value=200
  mock_debit.return_value=100
  assert  bank_obj.amount==mock_debit.return_value



