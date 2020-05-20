from app.src import app, db
from app.src.entity.music import Music
from app.src.entity.role import Role

from datetime import datetime

if __name__=='__main__':
    """
    music = Music(name='music_1', input_date=datetime(2020, 1, 5), release_date=datetime(2019, 2, 3))
    music1 = Music(name='music_2', input_date=datetime(2010, 1, 5), release_date=datetime(2017, 2, 3))
    music2 = Music(name='music_3', input_date=datetime(2018, 1, 5), release_date=datetime(2016, 2, 3))

    db.session.add(music)
    db.session.add(music1)
    db.session.add(music2)
    db.session.commit()
    """
    Role.insert_roles()
    app.run(debug = True)
