from . import erorr_handlers

class no_data(object):
  @classmethod
  def Q(cls, other):
    return other is cls

def dict_molding(data, models):
  res = {}
  for key, value in models.items():
    if not hasattr(data, key):
      if value[0]:
        raise Exception
      continue
    for x in value[1]:
      if type(data[key]) == x:
        break
    else:
      raise Exception
    res[key] = data[key]
  return res

def get_path(name):
  return ''.join(map(lambda x: '/' + x, name.split('.')[1:]))