from app import db


class Task(db.Model):
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        title = db.Column(db.String)
        description = db.Column(db.String)
        completed_at = db.Column(db.DateTime, nullable=True)



        def to_dict(self):
                is_complete = False if self.completed_at == None else True
                return {
                "id": self.id,
                "title": self.title,
                "description": self.description,
                "is_complete": is_complete,
                }
                


