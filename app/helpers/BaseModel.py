from app.helpers import queries

class BaseModel:
  def __init__(self, modelClass, data):
    table_name = type(modelClass).__name__
    columns = queries.getColumns(table_name)
    self.columns = []
    for column in columns:
      self.columns.append(TableInfo(column))

    for (i, column) in enumerate(self.columns):
      self.__setattr__(column.name, data[i])

  def serialize(self):
    properties = self.__dict__
    del properties['columns']
    return properties

class TableInfo:
  def __init__(self, infos):
    self.name = infos[0]
    self.type = infos[1]
    self.nullable = False if infos[2] == 'NO' else True
    self.key = infos[3]
    self.default = infos[4]
    self.extra = infos[5]
