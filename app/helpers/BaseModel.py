from app.helpers import queries

class BaseModel:
  def __init__(self, modelClass, data):
    self.table_name = type(modelClass).__name__
    column_infos = queries.getColumns(self.table_name)
    for (i, column_info) in enumerate(column_infos):
      self.__setattr__(column_info[0], data[i])

  def serialize(self):
    properties = self.__dict__
    del properties['table_name']
    return properties
