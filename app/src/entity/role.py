from app.src import db


class Permission:
    FOLLOW = 0b00000001
    COMMENT = 0b00000010
    MODERATE = 0b00000100
    ADMINISTER = 0b00001000


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', back_populates='role_object')

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.FOLLOW | Permission.COMMENT, True),
            'Moderator': (Permission.FOLLOW | Permission.COMMENT | Permission.MODERATE, False),
            'Administrator': (Permission.FOLLOW | Permission.COMMENT | Permission.MODERATE | Permission.ADMINISTER, False)
        }

        for r in roles:
            role = Role.query.filter_by(name=r).first()

            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]

            db.session.add(role)
        db.session.commit()
