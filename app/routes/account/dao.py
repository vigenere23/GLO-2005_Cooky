from app import db
from .model import AccountModel
from app.helpers.BaseDao import BaseDao

class AccountDao(BaseDao):

    def __init__(self):
        super().__init__('Account', AccountModel)

    def getAccountByUserId(self, id_User):
        query = 'SELECT * FROM Account WHERE id_User = %(id_User)s'
        result = db.select(query, {'id_User': id_User}, limit=1)
        return self._mapper.from_tuple(result)

    def modifyFirstName(self, firstName, id_User):
        query = 'UPDATE Account SET firstName = \'{}\' WHERE id_User = {}'.format(firstName, id_User)
        db.modify(query, {'id_User': id_User, 'firstName': firstName})
        return {"id_User": id_User, "firstName": firstName}

    def modifyLastName(self, lastName, id_User):
        query = 'UPDATE Account SET lastName = \'{}\' WHERE id_User = {}'.format(lastName, id_User)
        db.modify(query, {'id_User': id_User, 'lastName': lastName})
        return {"id_User": id_User, "lastName": lastName}

    def modifyEmail(self, email, id_User):
        query = 'UPDATE Account SET email = \'{}\' WHERE id_User = {}'.format(email, id_User)
        db.modify(query, {'id_User': id_User, 'email': email})
        return {"id_User": id_User, "email": email}

    def modifyPassword(self, password, id_User):
        query = 'UPDATE Account SET password = \'{}\' WHERE id_User = {}'.format(password, id_User)
        db.modify(query, {'id_User': id_User, 'password': password})
        return {"id_User": id_User, "password": password}



    def save(self, accountModel):
        if not isinstance(accountModel, AccountModel):
            raise ValueError("accountModel should be of type AccountModel")

        query = 'INSERT INTO Account (id, id_User, id_Address, firstName, lastName, email, password) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        newAccount = db.insert(query, self._mapper.to_tuple(accountModel))
       
        if newAccount:
            return self.getById(newAccount)
        else:
            raise Exception("Could not save rate")