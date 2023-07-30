import uuid

import sqlalchemy as sa

from app import db


class User(db.Model):
    __tablename__ = 'users'

    user_id = sa.Column(sa.UUID, primary_key=True, default=uuid.uuid4)
    name = sa.Column(sa.String(100), nullable=False)
    email = sa.Column(sa.String(150), nullable=False)
    tasks = db.relationship('Task', backref='users')

    def serialize(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'email': self.email
        }

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def get(cls, user_id):
        return cls.query.get_or_404(user_id)

    @classmethod
    def create(cls, data):
        user = cls()
        user.name = data['name']
        user.email = data['email']
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def update(cls, user_id, data):
        user = cls.get(user_id)
        if 'name' in data:
            user.name = data['name']
        if 'email' in data:
            user.email = data['email']
        db.session.commit()
        return user

    @classmethod
    def delete(cls, user_id):
        user = cls.get(user_id)
        db.session.delete(user)
        db.session.commit()
        return user
