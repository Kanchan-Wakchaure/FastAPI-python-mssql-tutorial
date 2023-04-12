from sqlalchemy.orm import Session

import models, schemas

def get_persons(db: Session, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Person)
        .order_by(models.Person.id)
        .offset(skip)
        .limit(limit)
        .all()
    )

def create_person(db: Session, person: schemas.PersonCreate):
    db_person = models.Person(**person.dict())
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person
