class BaseDao:
  
  def getAll(self):
    raise NotImplementedError()

  def getById(self):
    raise NotImplementedError()    

  def save(self):
    raise NotImplementedError()

  def replace(self):
    raise NotImplementedError()

  def delete(self):
    raise NotImplementedError()
