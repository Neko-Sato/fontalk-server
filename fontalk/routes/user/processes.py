from . import view

class create(view.firebase_view):
  def view(self, data, firebase_id, *args, **kwargs):
      return 'create', None