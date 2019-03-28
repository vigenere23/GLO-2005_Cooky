from app.helpers.BaseModel import BaseModel

class AddressModel(BaseModel):
  def __init__(self, id=None, number=None, appartment=None, street=None, city=None, country=None):
    self.id = id
    self.number = number
    self.appartment = appartment
    self.street = street
    self.city = city
    self.country = country