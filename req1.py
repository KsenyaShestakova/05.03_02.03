from data.db_session import global_init, create_session
from data.user import User

database_name = input()
global_init(database_name)
session = create_session()
users = session.query(User).filter(User.address == 'module_1',
                                   User.speciality.notlike('%engineer%')
                                   and User.position.notlike('%engineer%')).all()

print(*map(lambda user: user.id, users), sep='\n')
session.close()