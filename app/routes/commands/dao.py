from app import db
from .model import CommandModel
from app.helpers.BaseDao import BaseDao

class CommandDao(BaseDao):

    def __init__(self):
        super().__init__('Command', CommandModel)

    def getCommandByCart(self, id_Cart):
        query = 'SELECT * FROM Command WHERE id_Cart = %(id_Cart)s'
        results = db.select(query, {'id_Cart': id_Cart})
        return self._mapper.from_tuples(results)
    
    def save(self, commandsModel):
        if not isinstance(commandsModel, CommandModel):
            raise ValueError("commandsModel should be of type CommandModel")
        
        query = 'INSERT INTO Command (id, id_Cart, creationDate, arrivalDate) VALUES (%s, %s, %s, %s)'
        newCommand = db.insert(query, self._mapper.to_tuple(commandsModel))

        if newCommand:
            return self.getById(newCommand)
        else:
            raise Exception("Could not add newCommand")