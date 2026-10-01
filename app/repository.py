from sqlalchemy.orm import Session

from . import models, schemas


def get_all(db: Session):
    return db.query(models.Member).order_by(models.Member.name).all()


def get_by_id(db: Session, member_id: str):
    return db.query(models.Member).filter(models.Member.id == member_id).first()


def create(db: Session, data: schemas.MemberCreate):
    member = models.Member(**data.model_dump())
    db.add(member)
    db.commit()
    db.refresh(member)
    return member


def update(db: Session, member: models.Member, data: schemas.MemberUpdate):
    values = data.model_dump(exclude_unset=True)
    for field, value in values.items():
        setattr(member, field, value)

    db.commit()
    db.refresh(member)
    return member


def delete(db: Session, member: models.Member):
    db.delete(member)
    db.commit()


def delete_all(db: Session):
    count = db.query(models.Member).delete()
    db.commit()
    return count
