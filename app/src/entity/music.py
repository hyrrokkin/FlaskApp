from app.src import db


class Music(db.Model):
    __tablename__ = 'music'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    input_date = db.Column(db.DateTime, nullable=True)
    release_date = db.Column(db.DateTime, nullable=True)

    @staticmethod
    def load_by_name(name):
        return Music.query.filter_by(name=name)

    @staticmethod
    def sort_by_input_date():
        return Music.query.order_by(Music.input_date.asc()).all()

    def __repr__(self):
        return "Music {} {} {} {}\n".format(self.id, self.name, self.input_date, self.release_date)

    def serialize(self):
        return {
                'id': self.id,
                'name': self.name,
                'input_date': self.input_date,
                'release_date': self.release_date
            }

