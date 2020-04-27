from app.src import app
from app.src.entity.role import Role

if __name__=='__main__':
    Role.insert_roles()
    app.run(debug = True)
