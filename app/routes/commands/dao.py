from app import db
from .model import CommandsModel
from app.helpers.BaseDao import BaseDao
from app.helpers.SQLMapper import SQLMapper
from app.helpers.exceptions import NotFoundException

class CommandsDao(BaseDao):

    def __init__(self):
        self.mapper = SQLMapper('Commands', CommandsModel)

    def getAll(self):
        query = 'SELECT * FROM Commands'
        results = db.select(query)
        return self.mapper.from_tuples(results)

    def getCommandByCart(self, id_Cart):
        query = 'SELECT * FROM Commands WHERE id_Cart = %(id_Cart)s'
        results = db.select(query, {'id_Cart': id_Cart})
        return self.mapper.from_tuples(results)

    
    def save(self, commandsModel):
        if not isinstance(commandsModel, CommandsModel):
            raise ValueError("commandsModel should be of type CommandsModel")
        pass