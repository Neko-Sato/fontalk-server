from .models import *
from .erorr_handlers import *

def test(user_id):
  temp = {\
    'message': 'Your ID is {}'.format(user_id), \
  }
  return temp

def erorr():
  raise TestErorr('テストのエラーです')