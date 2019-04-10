from app import db
from .model import ProfileModel
from app.helpers.BaseDao import BaseDao

class ProfileDao(BaseDao):

    def __init__(self):
        super().__init__('Profile', ProfileModel)

    def getProfileByUser(self, id_User):
        query = 'SELECT * FROM Profile WHERE id_User = %(id_User)s'
        results = db.select(query, {'id_User': id_User})
        return self._mapper.from_tuples(results)
    
    def save(self, profileModel):
        if not isinstance(profileModel, ProfileModel):
            raise ValueError("profileModel should be of type ProfileModel")
        pass