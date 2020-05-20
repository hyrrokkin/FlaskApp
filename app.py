from app.src import app, db
from app.src.entity.music import Music
from app.src.entity.role import Role

from datetime import datetime

if __name__=='__main__':
    """    
    music = Music(
        name='Soul Rebels',
        performer='Боб Марли',
        genre='Регги',
        input_date=datetime(1970, 12, 5),
        release_date=datetime.utcnow(),
        cover='reg12334g1.jpeg'
    )

    music1 = Music(
        name='Soul Revolution',
        performer='Боб Марли',
        genre='Регги',
        input_date=datetime(1970, 12, 5),
        release_date=datetime.utcnow(),
        cover='beg2323ty34.jpeg'
    )

    music2 = Music(
        name='The Best of the Wailers',
        performer='Боб Марли',
        genre='Регги',
        input_date=datetime(1970, 12, 5),
        release_date=datetime.utcnow(),
        cover='fh421kge239gef2.jpeg'
    )

    db.session.add(music)
    db.session.add(music1)
    db.session.add(music2)
    db.session.commit()
    """
    Role.insert_roles()
    app.run(debug = True)
