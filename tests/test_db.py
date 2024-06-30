from sqlalchemy import create_engine, select

from fast_zero.models import User


def test_create_user():
    engine = create_engine(session)

    table_registry.metadata.createl_all(engine)

    with Session(engine) as session:
        user = User(
            username='dunossauro',
            email='duno@ssauro.com',
            password='minha_senha-legal'
        )

        session.add(user)
        session.commit()

        session.scalar(
            select(User).where(User.email == 'duno@ssauro.com')
        )

    assert result.username == 'dunossauro'
