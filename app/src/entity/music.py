from app.src import db


class Music(db.Model):
    __tablename__ = 'music'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    performer = db.Column(db.String(64))
    genre = db.Column(db.String(64))
    input_date = db.Column(db.DateTime, nullable=True)
    release_date = db.Column(db.DateTime, nullable=True)
    cover = db.Column(db.String(64), nullable=True)
    tracks = db.relationship('Track', back_populates='album_object')

    @staticmethod
    def load_by_name(name):
        return Music.query.filter_by(name=name)

    @staticmethod
    def load_by_id(_id):
        return Music.query.filter_by(id=_id).first()

    @staticmethod
    def sort_by_input_date():
        return Music.query.order_by(Music.release_date.asc()).all()

    def __repr__(self):
        return "Music {} {} {} {}\n".format(self.id, self.name, self.input_date, self.release_date)

    def serialize(self):
        return {
                'id': self.id,
                'name': self.name,
                'input_date': self.input_date,
                'release_date': self.release_date
            }

