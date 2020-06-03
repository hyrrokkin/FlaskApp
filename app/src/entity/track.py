from app.src import db


class Track(db.Model):
    __tablename__ = 'tracks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    number = db.Column(db.Integer)
    file = db.Column(db.String(255))
    album = db.Column(db.Integer, db.ForeignKey('music.id'), nullable=False)
    album_object = db.relationship('Music', back_populates='tracks')

    @staticmethod
    def load_by_name(name):
        return Track.query.filter_by(name=name).all()

    @staticmethod
    def load_by_album(album):
        return Track.query.filter_by(album=album).all()
