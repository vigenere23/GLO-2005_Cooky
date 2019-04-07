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
        pass