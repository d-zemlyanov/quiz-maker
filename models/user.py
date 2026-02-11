from datetime import datetime


class User:

    def __init__(self, user_id, username, password, role, created_at=None):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role
        self.created_at = created_at or datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def to_dict(self) -> dict:
        return {
            'user_id': self.user_id,
            'username': self.username,
            'password': self.password,
            'role': self.role,
            'created_at': self.created_at
        }

    @classmethod
    def from_dict(cls, data: dict) -> User:
        return cls(
            user_id=data['user_id'],
            username=data['username'],
            password=data['password'],
            role=data['role'],
            created_at=data['created_at']
        )