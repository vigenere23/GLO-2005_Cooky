from app import db
from .model import CommandsModel
from app.helpers.BaseDao import BaseDao

class CommandsDao(BaseDao):

    def __init__(self):
        super().__init__('Commands', CommandsModel)

    def getCommandByCart(self, id_Cart):
        query = 'SELECT * FROM Commands WHERE id_Cart = %(id_Cart)s'
        results = db.select(query, {'id_Cart': id_Cart})
        return self._mapper.from_tuples(results)
    
    def save(self, commandsModel):
        if not isinstance(commandsModel, CommandsModel):
            raise ValueError("commandsModel should be of type CommandsModel")
        
        query = 'INSERT INTO Commands (id, id_Cart, creationDate, arrivalDate) VALUES (%s, %s, %s, %s)'
        newCommand = db.insert(query, self._mapper.to_tuple(commandsModel))

        if newCommand:
            return self.getById(newCommand)
        else:
            raise Exception("Could not add newCommand")