from .erorr_handlers import InvalidUsage

class no_data(object):
  @classmethod
  def Q(cls, other):
    return other is cls
  @classmethod
  def W(cls, other, value):
    return value if cls.Q(other) else other

def dict_molding(data, models):
  res = {}
  for key, value in models.items():
    if not hasattr(data, key):
      if value[0]:
        raise InvalidUsage('Required item {} does not exist'.format(key))
      else:
        temp = no_data
    elif not type(data[key]).__name__ in value[1]:
      raise InvalidUsage('Item {} is of the wrong type'.format(key))
    else:
      temp = data[key]
    res[key] = temp
  return res

def get_path(name):
  return ''.join(map(lambda x: '/' + x, name.split('.')[1:]))