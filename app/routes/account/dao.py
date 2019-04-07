from app import db
from .model import AccountModel
from app.helpers.BaseDao import BaseDao

class AccountDao(BaseDao):

    def __init__(self):
        super().__init__('Account', AccountModel)

    def save(self, accountModel):
        if not isinstance(accountModel, AccountModel):
            raise ValueError("accountModel should be of type AccountModel")
        pass