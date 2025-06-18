from bson import ObjectId

class User:
    def __init__(self, name, email, password, _id=None):
        self.id = str(_id) if _id else None
        self.name = name
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password
        }

    @classmethod
    def from_dict(cls, data):
        _id = data.get('_id') or data.get('id')
        return cls(
            name=data['name'],
            email=data['email'],
            password=data['password'],
            _id=_id
        )
