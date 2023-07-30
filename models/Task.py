import uuid

import sqlalchemy as sa

from app import db


class Task(db.Model):
    __tablename__ = 'tasks'

    id = sa.Column(sa.UUID, primary_key=True, default=uuid.uuid4)
    title = sa.Column(sa.String(100), nullable=False)
    description = sa.Column(sa.String(150), nullable=False)
    user_id = sa.Column(sa.UUID, sa.ForeignKey('users.user_id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'user_id': self.user_id
        }

    @classmethod
    def all(cls):
        return cls.query.all()

    @classmethod
    def get(cls, task_id):
        return cls.query.get_or_404(task_id)

    @classmethod
    def get_by_user(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()

    @classmethod
    def create(cls, user_id, data):
        task = cls()
        task.title = data['title']
        task.description = data['description']
        task.user_id = user_id
        db.session.add(task)
        db.session.commit()
        return task

    @classmethod
    def update(cls, task_id, data):
        task = cls.get(task_id)
        if 'title' in data:
            task.title = data['title']
        if 'description' in data:
            task.description = data['description']
        db.session.commit()
        return task

    @classmethod
    def delete(cls, task_id):
        task = cls.get(task_id)
        db.session.delete(task)
        db.session.commit()
        return task
