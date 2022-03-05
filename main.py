from flask import Flask
from data.db_session import global_init, create_session
from data.jobs import Jobs
from data.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init('db/users.db')
    session = create_session()
    user = User(surname="Ksenya",
                name="Shestakova",
                age=15,
                position="student",
                speciality="I",
                address="module_1",
                email="KsenyaShestakova@mars.org",
                hashed_password="0987")
    """job = Jobs(team_leader=1,
               job='deployment of residential modules 1 and 2',
               work_size=15,
               collaborators='2, 3',
               is_finished=False)"""
    session.add(user)
    session.commit()
    app.run()


if __name__ == '__main__':
    main()