from sqlalchemy import create_engine
from sqlalchemy.orm import Session

def conn(connection_string: str):
    return create_engine(connection_string)


def save_legislatures(session: Session, legislatures: list):    
    session.add_all(legislatures)
    session.commit()
    
